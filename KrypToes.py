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

	def update_status(self):
		"""Update the price/value of each cryptocurrency, total value of the porfolio, and the corresponding meme."""
		#TODO
		pass

	def memeify(self, percent_change):
		"""Take the percent change of the cryptocurrency price and generate a customized meme."""
		#TODO
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
		#TODO
		pass

	def sell_crypto(self):
		"""Let the user to sell cryptocurrency in the current porfolio."""
		#TODO
		pass


if __name__ == "__main__":
	app = KrypToes()
