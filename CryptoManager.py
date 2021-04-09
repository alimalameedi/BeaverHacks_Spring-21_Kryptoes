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
		self._database_connection = self.connect_database()

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
		# TO DO

		# If database does not already exists, create one.
		# table for user data: user_id, username (string), hashed_password (string), cash_amount (float)


		# Connect to the database
		connection = sqlite3.connect("KrypToes.db")
		cursor = connection.cursor()

		# left out username and userid for now
		# table for porfolio: user_id, cryptocurrency_id (integer), holding (float)
		cursor.execute("""CREATE TABLE portfoliio (
		              crypto_name text,
		              crypto_id int,
		              holding float
		              )""")

		connection.commit()

		return connection

	def get_data(self, crypto_name):
		"""
		Takes the name of the cryptocurrency as a parameter and returns the user's data of
		that particular crypto holding

		:param crypto_name: the name of the cryptocurrency
		:return: data of user's cryptocurrency
		"""

		# create cursor
		cursor = self._database_connection.cursor()

		# obtain and return data
		cursor.execute("SELECT * FROM wallet WHERE cryptocurrency='%s'" % crypto_name)
		data = cursor.fetchall()
		return data


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
		# TO DO

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
