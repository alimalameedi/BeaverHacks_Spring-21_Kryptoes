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

		# Display a button for adding crypto
		self._add_crypto_button = Button(self._root, text="Get Price", command=self.lookup_price)
		self._add_crypto_button.pack(side=TOP, anchor=NW)

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


	def memeify(self):
		"""Take the percent change of the cryptocurrency price and generate a customized meme."""
		# TO DO
		pur_coin_amt=1
		act_coin_val=100
		pur_coin_val=200

		percent_change = (pur_coin_amt * act_coin_val)/pur_coin_val
		# Determine a meme that correspond to the percentage change for each cryptocurrency in the portfolio
		if pur_coin_amt * act_coin_val != pur_coin_val:

			if percent_change >= 2:  # if current amt is equal to or greater than 100% of buying price
				img1 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler5.png')))
				label.configure(image=img1)
				label.image = img1

			elif 2 > percent_change >= 1.75:
				img2 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler4.png')))
				label.configure(image=img2)
				label.image = img2

			elif 1.75 > percent_change >= 1.50:
				img3 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler3.png')))
				label.configure(image=img3)
				label.image = img3

			elif 1.50 > percent_change >= 1.25:
				img4 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler2.png')))
				label.configure(image=img4)
				label.image = img4

			elif 1.25 > percent_change > pur_coin_val:
				img5 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler1.png')))
				label.configure(image=img5)
				label.image = img5

			elif pur_coin_val > percent_change >= .80:
				img6 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown1.png')))
				label.configure(image=img6)
				label.image = img6

			elif .80 > percent_change >= .60:
				img7 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown2.png')))
				label.configure(image=img7)
				label.image = img7

			elif .60 > percent_change >= .40:
				img8 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown3.png')))
				label.configure(image=img8)
				label.image = img8

			elif .40 > percent_change >= .20:
				img9 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown4.png')))
				label.configure(image=img9)
				label.image = img9

			elif .20 > percent_change >= .5:
				img10 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown5.png')))
				label.configure(image=img10)
				label.image = img10

			elif .5 > percent_change:
				img11 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown6.png')))
				label.configure(image=img11)
				label.image = img11

		return label.image

	def update_status(self):
		"""Update the price/value of each cryptocurrency, total value of the porfolio, and the corresponding meme."""
		# TO DO

		# Query the current price for each cryptocurrency in the porfolio

		# Calculate the percent change in price for each cryptocurrency against the initial purchase price

		# Update each element in the display with the updated information
		#   unit price, % change in porfolion value, % change in the last hour, login status...

		class Coin:
			def __init__(self, name, numbought, buyprice):
				self.name=name
				self.numbought=numbought
				self.buyprice=buyprice

			def get_name(self):
				return self.name

			def get_numbought(self):
				return self.numbought

			def get_buyprice(self):
				return self.buyprice

		bitcoinval=50000

		given_data=[{cryptoname:bitcoin, coinsbought:1, buyprice:500, currentprice:bitcoinval}]

		for item in given_data:

			name=item[cryptoname]
			numbought=item[coinsbought]
			buyprice=item[currentprice]

			item[cryptoname] = Coin(name, numbought, buyprice)

			main_img = memeify()









		# Update the meme. calling the memeify method
		make_frame = LabelFrame(root, text="Sample Image", width=100, height=100)
		make_frame.pack()

		stim_filename = self.memeify()

		# create the PIL image object:
		PIL_image = Image.open(stim_filename)

		width = 100
		height = 100

		# You may prefer to use Image.thumbnail instead
		# Set use_resize to False to use Image.thumbnail
		use_resize = True

		if use_resize:
			# Image.resize returns a new PIL.Image of the specified size
			PIL_image_small = PIL_image.resize((width, height), Image.ANTIALIAS)
		else:
			# Image.thumbnail converts the image to a thumbnail, in place
			PIL_image_small = PIL_image
			PIL_image_small.thumbnail((width, height), Image.ANTIALIAS)

		# now create the ImageTk PhotoImage:
		img = ImageTk.PhotoImage(PIL_image_small)
		in_frame = Label(make_frame, image=img)
		in_frame.pack()

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
