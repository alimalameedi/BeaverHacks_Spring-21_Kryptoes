from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3
import csv


class CryptoManager():
	"""Backend of the Kryp-Toes application to manage the cryptocurrency porfolio
	and connect to an online server for the most up-to-date information."""

	def __init__(self):
		"""Instantiate the manager object for managing the account balance and cryptocurrency porfolio.
		Connect to the server and SQL database."""

		# Create and initialize data members to connect to server
		self._api_key = None
		self._url = None
		self._header = None
		self._session = None
		self.connect_server()

		# Data member for database connection
		self._database_connection = None
		self.connect_database()

		# Load id and name reference of the top 100 cryptocurrency
		self._crypto_name = {}
		self._crypto_id = {}
		self.load_crypto_reference()

	def connect_server(self):
		"""Connect to the server for the most up-to-date cryptocurrency pricing information."""

		# Get the API key from a file
		with open('API_key.txt', 'r') as reader:
			self._api_key = reader.read()
		reader.close()

		# Connect to the server (coinmarketcap.com)
		self._url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
		self._header = {
			"Accepts": "application/json",
			"X-CMC_PRO_API_KEY": self._api_key,
		}
		self._session = Session()
		self._session.headers.update(self._header)

	def connect_database(self):
		"""Connect to database to store user cash amount and cryptocurrency portfolio."""

		# Connect to the database
		self._database_connection = sqlite3.connect("Kryptoes.db")
		cursor = self._database_connection.cursor()

		# Create table for the portfolio if it does not already exist
		cursor.execute("""CREATE TABLE IF NOT EXISTS portfolio (
							user_id int NOT NULL,
							crypto_id int NOT NULL,
							quantity float NOT NULL,
							price float NOT NULL
						)""")

		# Create table that keeps track of the cash amount the user has on hand
		cursor.execute("""CREATE TABLE IF NOT EXISTS account (
							id INTEGER PRIMARY KEY,
							user_name text NOT NULL,
							cash_amount float NOT NULL
						)""")

		self._database_connection.commit()

	def load_crypto_reference(self):
		"""Load id and name references of the top 100 cryptocurrency and saved to dictionaries."""

		with open("crypto_reference.csv", newline='', encoding='utf-8') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				id, name = int(row[0]), row[1]
				self._crypto_name[id] = name
				self._crypto_id[name.lower()] = id

	def add_to_portfolio(self, user_id, crypto_id, quantity, price):
		"""Take user id, cryptocurrency id, quantity of the crypto to be purchase/sell, the price at the time of transaction as parameters. Adds the transaction of the cryptocurrency to user's portfolio"""

		# Connect to database
		with self._database_connection as connection:
			# append purchase/sell to portfolio
			connection.execute("INSERT INTO portfolio "
			                   "VALUES (:user_id, :crypto_id, :quantity, :price)",
			                   {
				                   "user_id": user_id,
				                   "crypto_id": crypto_id,
				                   "quantity": quantity,
				                   "price": price
			                   })

	def get_quantity(self, user_id, crypto_id):
		"""Take the user id, cryptocurrency id as parameters and
		return the quantity of that cryptocurrency that the user holds.
		Quantity of any cryptocurrency should never be less than zero."""

		with self._database_connection as connection:
			cursor = connection.execute("SELECT sum(quantity) from portfolio "
			                            "WHERE user_id=? AND crypto_id=?",
			                            (user_id, crypto_id,))

		return cursor.fetchone()[0]

	def get_prices(self, user_id, crypto_id):
		"""Take the user id, the cryptocurrency id as parameters and
		return a list of all transactions of that cryptocurrency that the user made.
		Each transaction is represented as a 2-tuple:
			(quantity, price at the time of transaction)
			A positive quantity represents a purchase, whereas
			A negative quantity represents a sell."""

		with self._database_connection as connection:
			cursor = connection.execute("SELECT quantity, price from portfolio "
			                            "WHERE user_id=? AND crypto_id=?",
			                            (user_id, crypto_id,))

		return cursor.fetchall()

	def create_account(self, username, cash_amount):
		"""Take username and cash amount as parameter and
		create an user account in the database."""

		with self._database_connection as connection:
			cursor = connection.execute("INSERT INTO account(user_name, cash_amount) "
			                            "VALUES (:user_name, :cash_amount)",
			                            {
				                            "user_name": username,
				                            "cash_amount": cash_amount
			                            })

	def hash_password(self, password):
		"""Encrypt the password."""
		# BONUS
		pass

	def authenticate(self, username, hashed_password):
		"""Take username and password as parameter and authenticate the current user."""
		# BONUS
		pass

	def lookup_crypto_id(self, crypto_name):
		"""Take the name of the cryptocurrency as parameter and
		return the id of the currency according to coinmarketcap.com"""

		return self._crypto_id[crypto_name.lower()]

	def lookup_crypto_name(self, crypto_id):
		"""Take the id of the cryptocurrency (according to coinmarketcap.com) as parameter and
		return the name of the currency"""

		return self._crypto_name[crypto_id]

	def get_current_price(self, crypto_id, get_percent_change=False):
		"""Take the id of the cryptocurrency as parameter.
		Query and return the most up-to-date price of that cryptocurrency."""

		# Parameters for Query
		parameters = {
			"start": crypto_id,
			"limit": "1",
			"convert": "USD"
		}

		# Pull cryptocurrency data from the server
		try:
			response = self._session.get(self._url, params=parameters)
			data = json.loads(response.text)

			# If the no need for getting the percent change, then just return the current price
			if not get_percent_change:
				return data["data"][0]["quote"]["USD"]["price"]

			# If the percent change is needed, then return (current price, percent change in the last hour)
			else:
				return (data["data"][0]["quote"]["USD"]["price"], data["data"][0]["quote"]["USD"]["percent_change_1h"])

		# Handle all connection errors
		except (ConnectionError, Timeout, TooManyRedirects) as error_message:
			print(error_message)

	def get_cash_amount(self, user_id):
		"""Take the user id as a parameter and return the cash amount currently have on hand."""
		with self._database_connection as connection:
			cursor = connection.execute("SELECT cash_amount from account "
			                            "WHERE id=?", (user_id,))

		return cursor.fetchone()[0]

	def update_cash_amount(self, user_id, change_amount):
		"""Take the user id as a parameter and update the cash ammount currently in the account."""

		cash_before_change = self.get_cash_amount(user_id)
		cash_after_change = cash_before_change + change_amount

		with self._database_connection as connection:
			cursor = connection.execute("UPDATE account "
			                            "SET cash_amount=? "
			                            "WHERE id=?",
			                            (cash_after_change, user_id))

	def buy_crypto(self, user_id, crypto_id, units):
		"""Take the user id, cryptocurrency id, and units to invest as parameters and make the purchase. Return a 2-tuple (units, value) if the purchase is successful."""

		# Ensure the user has enough cash on hand
		cash = self.get_cash_amount(user_id)
		price = self.get_current_price(crypto_id)
		if cash < price * units:
			raise InsufficientFundError

		value = price * units

		# Make the purchase
		#   decrease the cash_amount
		self.update_cash_amount(user_id, -value)

		#   update the holding for the cryptocurrency
		self.add_to_portfolio(user_id, crypto_id, units, price)

		return (units, value)

	def sell_crypto(self, user_id, crypto_id, units):
		"""Take the user id, cryptocurrency id, and units to be sold as parameters and make the sell. Return a 2-tuple (units, value) if the sell is successful."""

		# Ensure the user has enough cryptocurrency to be sold
		holding = self.get_quantity(user_id, crypto_id)

		if holding is None or holding < units:
			raise InsufficientQuantityError

		price = self.get_current_price(crypto_id)

		# Make the sell
		#   increase the cash_amount

		value = price * units
		self.update_cash_amount(user_id, value)

		#   update the holding for the cryptocurrency
		self.add_to_portfolio(user_id, crypto_id, -units, price)

		return (units, value)

	def get_portfolio(self, user_id):
		"""Take the user id as a parameter and returns the entire portfolio as a dictionary."""

		# Initiate an empty dictionary to contain the user's current portfolio
		portfolio = {}

		with self._database_connection as connection:

			# Find all distinct cryptocurrency transaction that the user ever made
			cursor = connection.execute("SELECT DISTINCT crypto_id FROM portfolio "
			                            "WHERE user_id=?", (user_id,))

			# For every distinct cryptocurrency, find the quantity that the user hold
			for crypto in cursor.fetchall():
				crypto_id = crypto[0]
				quantity = self.get_quantity(user_id, crypto_id)

				# Only add to the portfolio dictionary if the quantity is above zero
				if quantity > 0:
					portfolio[crypto_id] = quantity

		return portfolio

	def get_each_crypto_value(self, user_id, crypto_id):
		"""Take the user id and the cryptocurrency id as parameters and
		returns the value (in US dollar) of the cryptocurrency."""

		quantity = self.get_quantity(user_id, crypto_id)
		price = self.get_current_price(crypto_id)

		return quantity * price

	def get_total_portfolio_value(self, user_id):
		"""Take the user id as a parameter and return the total worth of the portfolio."""

		portfolio = self.get_portfolio(user_id)

		total_value = 0
		for crypto_id in portfolio:
			total_value += self.get_each_crypto_value(user_id, crypto_id)

		return total_value

	def get_user_by_id(self, user_id):
		"""Take the user id as a parameter and get the user's information."""

		with self._database_connection as connection:
			cursor = connection.execute("SELECT * FROM account WHERE id=?", (user_id,))

			user_data = cursor.fetchone()

		return user_data


class InsufficientFundError(Exception):
	"""Raise when the user does not have enough fund to buy any cryptocurrency."""
	pass


class InsufficientQuantityError(Exception):
	"""Raise when the user does not have enough quantity of the cryptocurrency being sold."""
	pass


if __name__ == "__main__":
	# Test code
	app = CryptoManager()

	# Create a temporary user with initiate cash amount of $10,000.00
	# app.create_account("Elon", 10000.00)

	# Get the quantity of Bitcoin the user has
	# print(app.get_quantity(1, 1))

	# Get the purchase/sell prices of all transaction the user has made
	# print(app.get_prices(1, 1))

	# Get the current cash amount that the user has
	# print(app.get_cash_amount(1))
	#
	# Buy Bitcoin
	# app.buy_crypto(1, 1, 0.001)
	#
	# Attempt to buy too much bitcoin with insufficient cash
	# try:
	# 	app.buy_crypto(1, 1, 1)
	# except InsufficientFundError:
	# 	print("You are too poor to invest!")
	#
	# Attempt to sell bitcoin with insufficient quantity in the porfolio
	# try:
	# 	app.sell_crypto(1, 1, 1)
	# except InsufficientQuantityError:
	# 	print("You are don't even have enough to sell!")
	#
	# Sell Bitcoin
	# app.sell_crypto(1, 1, 0.0001)
	#
	# Get the quantity of Bitcoin the user currently has
	# print(app.get_quantity(1, 1))
	#
	# Buy some Ethereum and Dogecoin and sell some Bitcoin
	# app.buy_crypto(1, 2, 0.2)
	# app.buy_crypto(1, 19, 0.3)
	# app.sell_crypto(1, 1, 0.01)
	#
	# Get the entire porfolio of the user
	# print(app.get_portfolio(1))
	#
	# Get the value (quantity * price) of each cryptocurrency in the user's portfolio
	# print(app.get_each_crypto_value(1, 1))
	# print(app.get_each_crypto_value(1, 2))
	# print(app.get_each_crypto_value(1, 19))
	#
	# Get the total worth of the user's portfolio
	# print(app.get_total_portfolio_value(1))
	#
	# Get the current price and percentage change in the last hour
	# print(app.get_current_price(1, True))
	#
	# Get the entire portfolio of the user
	# print(app.get_portfolio(1))

	# Look up the id of Bitcoin
	# print(app.lookup_crypto_id("bitcoin"))

	# Look up the name of Bitcoin (id = 1)
	# print(app.lookup_crypto_name(1))

	app.get_user_by_id(1)
