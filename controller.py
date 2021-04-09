# Description: Controllers act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output. For example, the Customer controller will handle all the interactions and inputs from the Customer View and update the database using the Customer Model. The same controller will be used to view the Customer data. Retrieved from: https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm

from view import KryToesUI
from model import CryptoManager

class KrypToesApp:
	"""Represent the Kryp-Toes application. """

	def __init__(self, update_period=3600):
		""""Instantiate the KrypToes application."""
		pass

	def auto_update(self):
		pass




if __name__ == "__main__":
	app = KrypToesApp()