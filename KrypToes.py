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
	def __init__(self, app, assets):
		self._root = app.get_root()

		self._panels = [[]]
		self._row = 0
		self._col = 0

	def create_panel(self, crypto_name, image):
		"""
		Create panel for each of User's assets
		"""
		panel = Panel(self._root, crypto_name, image, self._row, self._col)
		panel.display()
		if self._col > 0:

			self._row += 1
			self._col = 0
		else:
			self._col += 1

	def update_panel(self):
		""" Updates all assets with new values """
		pass

class Panel:
	def __init__(self, root, crypto_name, image, row, col):
		self._root = root
		self._crypto_name = crypto_name
		self._image = image
		self._row = row
		self._col = col

	def display(self):
		labelFrame = LabelFrame(self._root, height = 200, width = 200, text = self._crypto_name, font = ("Verdana", 16, "bold"))
		labelFrame.grid(row = self._row, column = self._col, pady = 10, padx = 10)
		labelFrame.grid_propagate(0)

		price_label = Label(labelFrame, text = "$0.0000", font = ("Verdana", 8))
		price_label.place(x = 5, y = 0)

	def get_crypto_name(self):
		return self._crypto_name

	def set_image(self, image):
		self._image = image

if __name__ == "__main__":
	app = KrypToes()
	creator = PanelManager(app, 0)
	creator.create_panel("Bitcoin", None)
	creator.create_panel("Ethereum", None)
	creator.create_panel("DogeCoin", None)
	creator.create_panel("LiteCoin", None)
	app.get_root().mainloop()