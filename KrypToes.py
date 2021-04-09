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
		self._root.mainloop()

	def initiate_elements(self):

		# Name the app
		self._root.title("Kryp-Toes")

		# Display the first meme
		self._meme_img = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler1.png')))
		self._meme_label = Label(self._root, image=self._meme_img)
		self._meme_label.grid(row=0, column=1)

		# Display a button for searching the current price
		self._get_price_button = Button(self._root, text="Get Price", command=self.lookup_price)
		self._get_price_button.grid(row=1, column=1)

		# Display a button for buying
		# TO DO

		# Display a button for selling
		# TO DO

		# Display the current holding
		# TO DO

		# Display the percentage change in porfolio value
		# TO DO

		# Display the percentage change in the last hour (or some other time period)
		# BONUS

		# Display the login status (username, connection to server/database...)
		# BONUS


	def update_status(self):
		"""Update the price/value of each cryptocurrency, total value of the porfolio, and the corresponding meme."""
		# TO DO

		# Query the current price for each cryptocurrency in the porfolio

		# Calculate the percent change in price for each cryptocurrency against the initial purchase price

		# Update each element in the display with the updated information
		#   unit price, % change in porfolion value, % change in the last hour, login status...

		# Update the meme. calling the memeify method

		pass

	def memeify(self, percent_change):
		"""Take the percent change of the cryptocurrency price and generate a customized meme."""
		# TO DO

		# Determine a meme that correspond to the percentage change for each cryptocurrency in the porfolio
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


if __name__ == "__main__":
	app = KrypToes()
