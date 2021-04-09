# Description: The Model component corresponds to all the data-related logic that the user works with. This can represent either the data that is being transferred between the View and Controller components or any other business logic-related data. For example, a Customer object will retrieve the customer information from the database, manipulate it and update it data back to the database or use it to render data. Retrieved from: https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm

import sqlite3

class CryptoManager():

	def __init__(self, database):
		#TODO
		pass

	def create_database(self):
		#TODO
		pass

	def create_account(self, username, password, cash_amount):
		#BONUS
		pass

	def hash_password(self, password):
		#BONUS
		pass

	def authenticate(self, username, hashed_password):
		#BONUS
		pass

	def lookup_id(self, cryto_name):
		#BONUS
		pass

	def get_current_price(self, user_id):
		#TODO
		pass

	def buy_crypto(self, user_id, cryto_id, units):
		#TODO
		pass

	def sell_crypto(self, user_id, cryto_id, units):
		#TODO
		pass
