from tkinter import ttk
import threading
from ttkthemes import ThemedTk, THEMES
from ttkthemes import themed_tk as tk
import os
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
		self._root = ThemedTk(themebg=True)
		self.initiate_elements()

	def get_manager(self):
		return self._app

	def get_root(self):
		return self._root

	def initiate_elements(self):
		# root window
		self._root.set_theme('equilux')
		self._root.title("Cryp-toes!")


		self._root.wm_iconbitmap(path.join('images',"doggo.ico"))
		self._root.geometry("425x425")

		# Enter BTC value window
		enterButton = ttk.Button(self._root, text="Add cryptocurrency")
		enterButton.grid(row=0, column=0)

		enterButton = ttk.Button(self._root, text="Buy new cryptocurrency")
		enterButton.grid(row=0, column=1)

		# query
		query_btn = ttk.Button(self._root, text="Look up Price", command=self.lookup_price)
		query_btn.grid(row=0, column=2)



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
		self._popup.wm_iconbitmap(path.join('images', "doggo.ico"))
		self._popup_message = ttk.Label(self._popup, text="Enter the name of the cryptocurrency:")
		self._popup_message.grid(row=0, column=0)
		self._popup_input = Entry(self._popup)
		self._popup_input.grid(row=1, column=0)
		self._popup_search = ttk.Button(self._popup, text="Search", command=show_price)
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
		self._panel_list = []
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
		assets = {1: 100.11, 2: 2, 3: 50.20}
		names = {1: "Bitcoin", 2: "Ethereum", 3: "BinanceCoin"}
		amounts= {1: 5.7, 2: 8.9, 3: .33}

		# loop through each asset and retrieve the name, and value
		#threading.Timer(5.0, self.create_all_panels).start()
		self.clear_panels(self._panel_list)
		for crypto_id in assets:

			# retrieve value
			# value = self._manager.get_each_crypto_value(self._user_id, crypto_id)		# commented out so we do not use token
			value = assets[crypto_id]

			# retrieve name
			# crypto_name = self._manager.get_crypto_name(crypto_id)		# commented out so we do not use token
			crypto_name = names[crypto_id]

			crypto_amounts = amounts[crypto_id]

			self.create_panel(crypto_name, value, crypto_amounts)


	def clear_panels(self, list):
		for item in list:
			item.destroy_frame()

	def create_panel(self, crypto_name, value, crypto_amounts):
		"""
		Create panels for each of User's assets
		"""
		# create panel object
		panel = Panel(self._root, crypto_name, value, crypto_amounts, self._row, self._col)
		self._panel_list.append(panel)
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
		self._frame=None
		self._image_lable=None


	def destroy_frame(self):
		self._frame.destroy()
		self._image_lable.destroy()

	"""def __delete__(self, instance):
		del self._root
		del self._crypto_name
		del self._value
		del self._image
		del self._row
		del self._col"""

	def display(self):
		# Creates the frame in which the meme and data will go into
		labelFrame = LabelFrame(self._root, height = 200, width = 200, text = self._crypto_name)
		labelFrame.grid(row = self._row, column = self._col, pady = 10, padx = 10)
		labelFrame.grid_propagate(0)
		self._frame=labelFrame

		# displays the total value of the asset
		price_label = Label(labelFrame, text = "$" + str(round(self._value, 2)), font = ("Verdana", 8))
		price_label.place(x = 5, y = 0)

		# INSERT IMAGE WITHIN FRAME
		image_label = Label(self._root, image=self._image)
		image_label.photo = self._image
		image_label.grid(row = self._row, column = self._col)
		self._image_lable=image_label

if __name__ == "__main__":
	KrypToes = KrypToes()
	creator = PanelManager(KrypToes, KrypToes.get_manager(), 1)
	KrypToes.get_root().mainloop()