from CryptoManager import CryptoManager
from tkinter import *
from PIL import ImageTk, Image
from os import path

class KrypToes:
	"""Represent the GUI of the Kryp-Toes applications."""

	def __init__(self):
		"""Instantiate the KrypToes application."""

		# Connect to the backend
		self._app = CryptoManager()

		# Set up the GUI using tkinter
		self._root = Tk()
		self.initiate_elements()

	def get_manager(self):
		return self._app

	def get_root(self):
		return self._root

	def initiate_elements(self):
		pass

	def memeify(self):
		"""Take the percent change of the cryptocurrency price and generate a customized meme."""
		pass

	def update_status(self):
		"""Update the price/value of each cryptocurrency, total value of the porfolio, and the corresponding meme."""
		# TO DO

		# Query the current price for each cryptocurrency in the porfolio

		# Calculate the percent change in price for each cryptocurrency against the initial purchase price

		# Update each element in the display with the updated information
		#   unit price, % change in porfolion value, % change in the last hour, login status...
		pass

	def create_account(self):
		"""Create an account for the user to start trading cryptocurrency."""
		#BONUS
		pass

	def login(self):
		"""Let the user login using username and password."""
		#BONUS
		pass

	def lookup_price(self):
		"""Let the user to enter the name of the cryptocurrency and
		show the current price (per unit) of that cryptocurrency."""

		def show_price():
			"""Query the price of the cryptocurrency and show it in the popup window."""

			input = self._popup_input.get()

			# TO DO
			# Allow searching for the cryptocurrency id by its name

			price = self._app.get_current_price("1")
			message = f"The current price of {input} is ${price:.2f} per unit."
			self._popup_price = Label(self._popup, text=message)
			self._popup_price.grid(row=3, column=0)

		# Create a popup window to ask the user for which cryptocurrency to show the price
		self._popup = Toplevel()
		self._popup_message = Label(self._popup, text="Enter the name of the cryptocurrency:")
		self._popup_message.grid(row=0, column=0)
		self._popup_input = Entry(self._popup)
		self._popup_input.grid(row=1, column=0)
		self._popup_search = Button(self._popup, text="Search", command=show_price)
		self._popup_search.grid(row=2, column=0)
		self._popup.mainloop()

	def buy_crypto(self):
		"""Let the user to buy cryptocurrency with available fund."""
		# TO DO

		# Show popup window to ask the user what to buy and how much

		# Invoke CryptoManager.buy_crypto method

		# Show error message when the purchasing is invalid (not enough money)
		#   Fun Bonus: show a meme that the user is too broke to purchase

		# Fun Bonus: show a meme that user successfully make the purchase
		pass

	def sell_crypto(self):
		"""Let the user to sell cryptocurrency in the current porfolio."""
		# TO DO

		# Show popup window to ask the user what to sell and how much

		# Invoke CryptoManager.sell_crypto method

		# Show error message when the sell is invalid (not enough stock)
		#   Fun Bonus: show a meme that the user does not have enough holding to sell

		# Fun Bonus: show a meme that user successfully make the sell
		pass


class PanelManager:
	"""
	 Creates a updates the panels on the main page. Each Panel contains the name of the
	 User's asset, the current value of their asset, and the meme.
	"""
	def __init__(self, app, manager, user_id):
		"""
		:param app: the KrypToes front-end
		:param manager: the KrypToes back-end (CryptoManager.py)
		:param user_id: the id of the user currently using the application
		"""

		# get root window
		self._root = app.get_root()
		self._user_id = user_id

		# CryptoManager to get data from back-end database
		self._manager = manager

		# rows and cols to organize/format main page
		self._row = 0
		self._col = 0

		# create all panels on main page
		self.create_all_panels()

	def create_all_panels(self):
		"""
		Create all panels on the main page
		"""

		# retrieve user's portfolio from database
		# assets = self._manager.get_portfolio(self._user_id) 		# commented out so we do not use token

		# fake data so we do not use all our tokens
		assets = {1: 100.11, 2: 200.56, 3: 50.11}
		names = {1: "Bitcoin", 2: "Ethereum", 3: "BinanceCoin"}

		# loop through each asset and retrieve the name, and value
		for crypto_id in assets:

			# retrieve value
			# value = self._manager.get_each_crypto_value(self._user_id, crypto_id)		# commented out so we do not use token
			value = assets[crypto_id]

			# retrieve name
			# crypto_name = self._manager.get_crypto_name(crypto_id)		# commented out so we do not use token
			crypto_name = names[crypto_id]

			# None should be the image
			self.create_panel(crypto_name, value, None)



	def create_panel(self, crypto_name, value, image):
		"""
		Create panels for each of User's assets
		"""
		# create panel object
		panel = Panel(self._root, crypto_name, value, image, self._row, self._col)

		# display panel
		panel.display()

		# formats the row and column of the panel on the main page
		if self._col > 0:

			self._row += 1
			self._col = 0
		else:
			self._col += 1

	def update_panel(self):
		""" Updates all assets with new values. Honestly, we may not need this """
		pass

class Panel:
	""" A panel on the main page. Displays the asset name, the value, and the meme """
	def __init__(self, root, crypto_name, value, image, row, col):
		# the root window of the app
		self._root = root

		# what is displayed on the panel
		self._crypto_name = crypto_name
		self._value = value
		self._image = image

		# where the panel is on the main page
		self._row = row
		self._col = col

	def display(self):
		# Creates the frame in which the meme and data will go into
		labelFrame = LabelFrame(self._root, height = 200, width = 200, text = self._crypto_name, font = ("Verdana", 16, "bold"))
		labelFrame.grid(row = self._row, column = self._col, pady = 10, padx = 10)
		labelFrame.grid_propagate(0)

		# displays the total value of the asset
		price_label = Label(labelFrame, text = "$" + str(round(self._value, 2)), font = ("Verdana", 8))
		price_label.place(x = 5, y = 0)

		# TO-DO
		# INSERT IMAGE WITHIN FRAME


	def set_image(self, image):
		""" Honestly, we may not need this """
		self._image = image

if __name__ == "__main__":
	KrypToes = KrypToes()
	creator = PanelManager(KrypToes, KrypToes.get_manager(), 1)
	KrypToes.get_root().mainloop()