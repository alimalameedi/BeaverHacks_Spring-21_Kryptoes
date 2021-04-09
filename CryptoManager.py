from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3

class CryptoManager():
	"""Backend of the Kryp-Toes application to manage the cryptocurrency porfolio
	and connect to an online server for the most up-to-date information."""

	def __init__(self):
		"""Instantiate the manager object. Connect to the server and SQL database."""

		self.connect_server()
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
		#TODO
		pass

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
		#TODO
		pass

	def get_current_price(self, cryto_id):
		"""Take the id of the cryptocurrency as parameter.
		Query and return the most up-to-date price of that cryptocurrency."""

		parameters = {
			"start": cryto_id,
			"limit": "1",
			"convert": "USD"
		}

		try:
			response = self._session.get(self._url, params=parameters)
			data = json.loads(response.text)
			return data["data"][0]["quote"]["USD"]["price"]

		except (ConnectionError, Timeout, TooManyRedirects) as error_message:
			print(error_message)

	def buy_crypto(self, user_id, cryto_id, units):
		"""Take the user id, cryptocurrency id, and units to invest as parameters and make the purchase."""
		#TODO
		pass

	def sell_crypto(self, user_id, cryto_id, units):
		"""Take the user id, cryptocurrency id, and units to be sold as parameters and make the sell."""
		#TODO
		pass
