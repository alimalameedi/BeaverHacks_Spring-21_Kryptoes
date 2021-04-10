from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3

class CryptoManager():
	"""Backend of the Kryp-Toes application to manage the cryptocurrency porfolio
	and connect to an online server for the most up-to-date information."""

	def __init__(self):
		"""Instantiate the manager object. Connect to the server and SQL database."""

		# Create and initialize data members to connect to server
		self._api_key = None
		self._url = None
		self._header = None
		self._session = None
		self.connect_server()

		# Data member for database connection
		self._database_connection = None
		self.connect_database()

	def connect_server(self):
		"""Connect to the server for the most up-to-date information."""

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
		"""
		Connect to database

		:return: a tuple containing the connection
		"""

		# If database does not already exists, create one.
		# table for user data: user_id, username (string), hashed_password (string), cash_amount (float)
			# BONUS


		# Connect to the database
		self._database_connection = sqlite3.connect("Kryptoes.db")
		cursor = self._database_connection.cursor()

		# Create table for portfolio if it does not already exist
		cursor.execute("""CREATE TABLE IF NOT EXISTS portfolio (
							crypto_id int,
							crypto_name text,
							quantity float,
							price float
						)""")

		# Create table that keeps track of the cash amount the user has on hand
		cursor.execute("""CREATE TABLE IF NOT EXISTS account (
							user_id int,
							user_name text,
							cash_amount float
						)""")

		# May remove later if account login functionality is implemented
		# Create a temporary user with initiate cash amount of $10,000.00
		cursor.execute("INSERT INTO account "
		               "VALUES (:user_id, :user_name, :cash_amount)",
		               {
			               "user_id": 1,
			               "user_name": "Elon",
			               "cash_amount": 10000.00
		               })

		self._database_connection.commit()

	def add_to_portfolio(self, crypto_id, crypto_name, quantity, price):
		"""
		Adds a cryptocurrency to user's portfolio
		"""

		# Connect to database
		connection = self._database_connection
		cursor = connection.cursor()

		# append purchase to portfolio
		cursor.execute("INSERT INTO portfolio "
		               "VALUES (:crypto_id, :crypto_name, :quantity, :price)",
					{
						"crypto_id": crypto_id,
						"crypto_name": crypto_name,
						"quantity": quantity,
						"price": price
					})

		connection.commit()


	"""
	def get_total_cryptocurrencies(self):
		
		# Returns the total distinct cryptocurrencies user has in portfolio
	

		# connect to database
		connection = self._database_connection
		cursor = connection.cursor()

		# retrieve number of cryptocurrencies
		cursor.execute("SELECT COUNT() FROM wallet")
		total_crypto = cursor.fetchall()

		# returns the number of cryptocurrencies user has
		return total_crypto[0]
	"""

	def get_quantity(self, crypto_id):
		"""Take the id of the cryptocurrency as parameter and
		return the quantity of that cryptocurrency that the user holds.
		Quantity of any cryptocurrency should never be less than zero."""

		with self._database_connection as connection:
			cursor = connection.execute("SELECT sum(quantity) from portfolio "
		                                "WHERE crypto_id=?", (crypto_id,))

		return cursor.fetchone()[0]


	def get_prices(self, crypto_id):
		"""Take the id of the cryptocurrency as parameter and
		return a list of all transaction of that cryptocurrency that the user made.
		Each transaction is represented as a 2-tuple:
			(quantity, price at the time of transaction)
			A positive quantity represents a purchase, whereas
			A negative quantity represents a sell."""

		with self._database_connection as connection:
			cursor = connection.execute("SELECT quantity, price from portfolio "
			                            "WHERE crypto_id=?", (crypto_id,))

		return cursor.fetchall()


	def create_account(self, username, password, cash_amount):
		"""Create an user account."""
		#BONUS
		pass

	def hash_password(self, password):
		"""Encrypt the password."""
		#BONUS
		pass

	def authenticate(self, username, hashed_password):
		"""Take username and password as parameter and authenticate the current user."""
		#BONUS
		pass

	def lookup_id(self, cryto_name):
		"""Take the name of the cryptocurrency as parameter and
		return the id of the currency according to coinmarketcap.com"""
		# TO DO
		pass

	def get_current_price(self, cryto_id):
		"""Take the id of the cryptocurrency as parameter.
		Query and return the most up-to-date price of that cryptocurrency."""

		# Parameters for Query
		parameters = {
			"start": cryto_id,
			"limit": "1",
			"convert": "USD"
		}

		# Pull cryptocurrency data from the server
		try:
			response = self._session.get(self._url, params=parameters)
			data = json.loads(response.text)
			return data["data"][0]["quote"]["USD"]["price"]

		# Handle all connection errors
		except (ConnectionError, Timeout, TooManyRedirects) as error_message:
			print(error_message)

		# TO DO


	def buy_crypto(self, user_id, cryto_id, units):
		"""Take the user id, cryptocurrency id, and units to invest as parameters and make the purchase."""

		# Ensure the user has enough cash on hand

		# Make the purchase
		#   decrease the cash_amount
		#   query the current price of the cryptocurrency
		#   update the holding for the cryptocurrency
		#       make a new entry for every purchase? (to keep track of net gain/loss)
		pass

	def sell_crypto(self, user_id, cryto_id, units):
		"""Take the user id, cryptocurrency id, and units to be sold as parameters and make the sell."""
		# TO DO

		# Ensure the user has this cryptocurrency in porfolio
		# Ensure the user has enough units on hand to be sold

		# Make the sell
		#   decrease or delete the holding
		#   query the current price of the cryptocurrency
		#   increase the cash amount
		pass

if __name__ == "__main__":
	app = CryptoManager()
	print(app.get_prices(1))