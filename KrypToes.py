from tkinter import ttk
import os
from CryptoManager import CryptoManager, InsufficientFundError, InsufficientQuantityError
from tkinter import *
from ttkthemes import ThemedTk, THEMES
from PIL import ImageTk, Image
from os import path

class KrypToes:
	"""Represent the GUI of the Kryp-Toes applications."""

	def __init__(self):
		"""Instantiate the KrypToes application."""

		# Connect to the backend
		self._app = CryptoManager()

		if self._app.get_user_by_id(1) is None:
			self._app.create_account("Elon", 10000.00)

		# Set up the GUI using tkinter
		self._root = ThemedTk(themebg=True)
		self.initiate_elements()

	def get_manager(self):
		return self._app

	def get_root(self):
		return self._root

	def is_valid_crypto(self, crypto_name):
		"""
		ANYTHING THAT CALLS THIS FUNCTION SHOULD CATCH THE "KeyError"
		Checks if the name of the Crypto entered into the text entry is valid

		"""
		try:
			return self._app.lookup_crypto_id(crypto_name)
		except KeyError:
			return False

	def initiate_elements(self):
		# root window
		self._root.set_theme('equilux')
		self._root.title("Cryp-toes!")

		if "nt" == os.name:
			self._root.wm_iconbitmap(bitmap = "images/doggo.ico")
			self._root.geometry("700x300")

		# Search for crypto
		text_box = ttk.Entry(self._root, width = 15)
		text_box.grid(row = 0, column = 0, ipadx = 0)

		# Enter BTC value window
		buyButton = ttk.Button(self._root, text="Buy", command=lambda :self.buy_crypto(text_box.get()))
		buyButton.grid(row=0, column=1)

		sellButton = ttk.Button(self._root, text="Sell", command=lambda :self.sell_crypto(text_box.get()))
		sellButton.grid(row=0, column=2)

		# query
		query_btn = ttk.Button(self._root, text="Look Up Price", command=lambda :self.lookup_price(text_box.get()))
		query_btn.grid(row=0, column=3)


	def memeify(self, pur_val, amt_of_crypto):
		"""Take the percent change of the cryptocurrency price and generate a customized meme."""
		pur_coin_amt=amt_of_crypto
		act_coin_val=5
		pur_coin_val=pur_val

		percent_change = (pur_coin_amt * act_coin_val) / pur_coin_val
		# Determine a meme that correspond to the percentage change for each cryptocurrency in the portfolio
		if pur_coin_amt * act_coin_val != pur_coin_val:

			if percent_change >= 2:  # if current amt is equal to or greater than 100% of buying price
				image = Image.open(path.join('images', 'wrestler5.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image=ImageTk.PhotoImage(image)

			elif 2 > percent_change >= 1.75:
				image = Image.open(path.join('images', 'wrestler4.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif 1.75 > percent_change >= 1.50:
				image = Image.open(path.join('images', 'wrestler3.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif 1.50 > percent_change >= 1.25:
				image = Image.open(path.join('images', 'wrestler2.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif 1.25 > percent_change > pur_coin_val:
				image = Image.open(path.join('images', 'wrestler1.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif pur_coin_val > percent_change >= .80:
				image = Image.open(path.join('images', 'clown1.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif .80 > percent_change >= .60:
				image = Image.open(path.join('images', 'clown2.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif .60 > percent_change >= .40:
				image = Image.open(path.join('images', 'clown3.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif .40 > percent_change >= .20:
				image = Image.open(path.join('images', 'clown4.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif .20 > percent_change >= .5:
				image = Image.open(path.join('images', 'clown5.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

			elif .5 > percent_change:
				image = Image.open(path.join('images', 'clown6.png'))
				image = image.resize((110, 110), Image.ANTIALIAS)
				the_image = ImageTk.PhotoImage(image)

		return the_image


	def update_status(self):
		"""Update the price/value of each cryptocurrency, total value of the porfolio, and the corresponding meme."""
		# TO DO

		# Query the current price for each cryptocurrency in the porfolio

		# Calculate the percent change in price for each cryptocurrency against the initial purchase price

		# Update each element in the display with the updated information
		#   unit price, % change in  value, % change in the last hour, login status...
		pass

	def lookup_price(self, crypto_name):
		"""Let the user to enter the name of the cryptocurrency and
		show the current price (per unit) of that cryptocurrency."""

		# Create a popup window to ask the user for which cryptocurrency to show the price
		self._popup = Toplevel()

		crypto_id = self.is_valid_crypto(crypto_name)

		if crypto_id:

			# Ensure the name is has the correctly Capitalized.
			crypto_name = self._app.lookup_crypto_name(crypto_id)

			price = self._app.get_current_price(crypto_id)

			message = f"The current price of {crypto_name} is ${price:.2f} per unit."

		else:

			message = f"This cryptocurrency does not exist!"

		self._popup_message = Label(self._popup, text=message)
		self._popup_message.grid(row=0, column=0)

		self._popup.mainloop()


	def buy_crypto(self, crypto_name):
		"""Let the user to buy cryptocurrency with available fund."""

		# Create a popup window
		self._popup = Toplevel()

		crypto_id = self.is_valid_crypto(crypto_name)

		if crypto_id:

			# Ensure the name is has the correctly Capitalized.
			crypto_name = self._app.lookup_crypto_name(crypto_id)

			price = self._app.get_current_price(crypto_id)

			message = f"The current price of {crypto_name} is ${price:.2f} per unit."

		else:

			message = f"This cryptocurrency does not exist!"

		# Show the current price
		self._popup_message = Label(self._popup, text=message)
		self._popup_message.grid(row=0, column=0)

		if crypto_id:

			# User enters the quantity they want to buy
			self._popup_label = Label(self._popup, text="Purchase Quantity:")
			self._popup_label.grid(row=1, column=0)

			# User entry for quantity
			self._popup_input = Entry(self._popup)
			self._popup_input.grid(row=2, column=0)

			# Submit button
			self._popup_button = Button(self._popup, text="Submit", command=lambda:self.buy(1, crypto_id, float(self._popup_input.get()), self._popup))
			self._popup_button.grid(row=3, column=0)
			self._popup.mainloop()

		# Fun Bonus: show a meme that user successfully make the purchase

	def buy(self, user_id, crypto_id, quantity, window):
		"""Take user id, cryptocurrency id, quantity to buy, and the popup window object as parameters.
		Make the purchase and show how much was purchased.
		Otherwise, show the user that he/she has insufficient fund."""

		try:

			# Buy through cryptomanager
			transaction = self._app.buy_crypto(user_id, crypto_id, quantity)
			units, value = transaction
			crypto_name = self._app.lookup_crypto_name(crypto_id)
			receipt_message = f"You purchased {units:.2f} units of {crypto_name} for ${value:.2f}"

		except InsufficientFundError:

			# Show the user that he/she has insufficient fund.
			receipt_message = "You are too poor to invest this much!"

		# Add additional row to the popup window with the purchase detail or error message
		receipt = Label(window, text=receipt_message)
		receipt.grid(row=4, column=0)

	def sell_crypto(self, crypto_name):
		"""Let the user to sell cryptocurrency with available cryptocurrency."""

		# Create a popup window
		self._popup = Toplevel()

		crypto_id = self.is_valid_crypto(crypto_name)

		if crypto_id:
			# Ensure the name is has the correctly Capitalized.
			crypto_name = self._app.lookup_crypto_name(crypto_id)
			price = self._app.get_current_price(crypto_id)
			quantity_available = self._app.get_quantity(1, crypto_id)

			price_message = f"The current price of {crypto_name} is ${price:.2f} per unit."

			# If the user does not have this cryptocurrency in his/her portfolio
			if quantity_available is None or abs(quantity_available - 0) < 0.0000000:
				possible_sell = False
				availability_message = f"You don't have any of {crypto_name} to sell!"
			else:
				possible_sell = True
				availability_message = f"You currently have {quantity_available:.2f} units of {crypto_name} in your portfolio."

		else:
			price_message = f"This cryptocurrency does not exist!"

		# Show the current price or error message if the cryptocurrency does not exist
		self._popup_message = Label(self._popup, text=price_message)
		self._popup_message.grid(row=0, column=0)

		if crypto_id:

			# Show the availability of the cryptocurrency
			self._popup_message = Label(self._popup, text=availability_message)
			self._popup_message.grid(row=1, column=0)

			if possible_sell:

				# User enters the quantity they want to sell
				self._popup_label = Label(self._popup, text="Sell Quantity:")
				self._popup_label.grid(row=2, column=0)

				# User entry for quantity
				self._popup_input = Entry(self._popup)
				self._popup_input.grid(row=3, column=0)

				# Submit button
				self._popup_button = Button(self._popup, text="Submit", command=lambda: self.sell(1, crypto_id, float(self._popup_input.get()), self._popup))
				self._popup_button.grid(row=4, column=0)
				self._popup.mainloop()

		# Fun Bonus: show a meme that user successfully make the purchase

	def sell(self, user_id, crypto_id, quantity, window):
		"""Take user id, cryptocurrency id, quantity to buy, and the popup window object as parameters.
		Make the sell and show how much was sold.
		Otherwise, show the user that he/she has insufficient quantity."""

		try:
			# Sell through cryptomanager
			transaction = self._app.sell_crypto(user_id, crypto_id, quantity)
			units, value = transaction
			crypto_name = self._app.lookup_crypto_name(crypto_id)
			receipt_message = f"You sold {units:.2f} units of {crypto_name} for ${value:.2f}"

		except InsufficientQuantityError:

			# Show the user that he/she has insufficient quantity.
			receipt_message = "You don't have enough to sell this much!"

		# Add additional row to the popup window with the purchase detail or error message
		receipt = Label(window, text=receipt_message)
		receipt.grid(row=5, column=0)

		# Update available quantity for sell
		quantity_available = self._app.get_quantity(1, crypto_id)
		availability_message = f"You currently have {quantity_available:.2f} units of {crypto_name} in your portfolio."
		# Show the availability of the cryptocurrency
		self._popup_message = Label(self._popup, text=availability_message)
		self._popup_message.grid(row=1, column=0)


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
		self._row = 1
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
		assets = {1: 100.11, 2: 2, 3: 50.11}
		names = {1: "Bitcoin", 2: "Ethereum", 3: "BinanceCoin"}
		amounts= {1: 5.7, 2: 8.9, 3: .33}

		# loop through each asset and retrieve the name, and value
		for crypto_id in assets:

			# retrieve value
			# value = self._manager.get_each_crypto_value(self._user_id, crypto_id)		# commented out so we do not use token
			value = assets[crypto_id]

			# retrieve name
			# crypto_name = self._manager.get_crypto_name(crypto_id)		# commented out so we do not use token
			crypto_name = names[crypto_id]

			crypto_amounts = amounts[crypto_id]

			# None should be the image
			self.create_panel(crypto_name, value, crypto_amounts)



	def create_panel(self, crypto_name, value, crypto_amounts):
		"""
		Create panels for each of User's assets
		"""
		# create panel object
		panel = Panel(self._root, crypto_name, value, crypto_amounts, self._row, self._col)

		# display panel
		panel.display()

		# formats the row and column of the panel on the main page
		if self._col > 1:

			self._row += 1
			self._col = 0
		else:
			self._col += 1

	def update_panel(self):
		""" Updates all assets with new values. Honestly, we may not need this """
		pass

class Panel:
	""" A panel on the main page. Displays the asset name, the value, and the meme """
	def __init__(self, root, crypto_name, value, crypto_amounts, row, col):
		# the root window of the app
		self._root = root

		# what is displayed on the panel
		self._crypto_name = crypto_name
		self._value = value
		self._image = KrypToes.memeify(value, crypto_amounts)

		# where the panel is on the main page
		self._row = row
		self._col = col

	def display(self):
		# Creates the frame in which the meme and data will go into
		labelFrame = ttk.LabelFrame(self._root, height = 200, width = 200, text = self._crypto_name)
		labelFrame.grid(row = self._row, column = self._col, pady = 10, padx = 10)
		labelFrame.grid_propagate(0)

		# displays the total value of the asset
		price_label = ttk.Label(labelFrame, text = "$" + str(round(self._value, 2)))
		price_label.place(x = 5, y = 0)

		# INSERT IMAGE WITHIN FRAME
		image_label = Label(self._root, image=self._image)
		image_label.photo = self._image
		image_label.grid(row = self._row, column = self._col)



	def set_image(self, image):
		""" Honestly, we may not need this """
		self._image = image

if __name__ == "__main__":
	KrypToes = KrypToes()
	creator = PanelManager(KrypToes, KrypToes.get_manager(), 1)
	KrypToes.get_root().mainloop()