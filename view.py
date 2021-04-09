# Description: The View component is used for all the UI logic of the application. For example, the Customer view will include all the UI components such as text boxes, dropdowns, etc. that the final user interacts with. Retrieved from: https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm

# Description: Controllers act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output. For example, the Customer controller will handle all the interactions and inputs from the Customer View and update the database using the Customer Model. The same controller will be used to view the Customer data. Retrieved from: https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm

from model import CryptoManager
from controller import KrypToesApp
from tkinter import *

class KrypToesUI:
	"""Represent the GUI of the Kryp-Toes applications."""

	def __init__(self):
		"""Instantiate the Graphical User Interface."""
		pass

	def initiate_elements(self):
		pass

	def update_status(self):
		#TODO
		pass

	def create_account(self):
		#BONUS
		pass

	def login(self):
		#BONUS
		pass

	def lookup_price(self):
		#TODO
		pass

	def buy_crypto(self):
		#TODO
		pass

	def sell_crypto(self):
		#TODO
		pass



class KrypToesApp:
	"""Represent the Kryp-Toes application. """

	def __init__(self, update_period=3600):
		""""Instantiate the KrypToes application.
			Invoke the GUI and automatically update periodically."""
		pass

	def auto_update(self):
		"""Automatically update the GUI."""
		#TODO
		pass

	def login(self):
		pass


if __name__ == "__main__":
	app = KrypToesApp()


