from CryptoManager import CryptoManager
from tkinter import *
from PIL import ImageTk, Image
from os import path
root = Tk()

def memeify():
    """Take the percent change of the cryptocurrency price and generate a customized meme."""
    # TO DO
    pur_coin_amt = 1
    act_coin_val = 100
    pur_coin_val = 200

    percent_change = (pur_coin_amt * act_coin_val) / pur_coin_val
    # Determine a meme that correspond to the percentage change for each cryptocurrency in the portfolio
    if pur_coin_amt * act_coin_val != pur_coin_val:

        if percent_change >= 2:  # if current amt is equal to or greater than 100% of buying price
            img1 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler5.png')))
            Label.configure(image=img1)
            Label.image = img1

        elif 2 > percent_change >= 1.75:
            img2 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler4.png')))
            Label.configure(image=img2)
            Label.image = img2

        elif 1.75 > percent_change >= 1.50:
            img3 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler3.png')))
            Label.configure(image=img3)
            Label.image = img3

        elif 1.50 > percent_change >= 1.25:
            img4 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler2.png')))
            Label.configure(image=img4)
            Label.image = img4

        elif 1.25 > percent_change > pur_coin_val:
            img5 = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler1.png')))
            Label.configure(image=img5)
            Label.image = img5

        elif pur_coin_val > percent_change >= .80:
            img6 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown1.png')))
            Label.configure(image=img6)
            Label.image = img6

        elif .80 > percent_change >= .60:
            img7 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown2.png')))
            Label.configure(image=img7)
            Label.image = img7

        elif .60 > percent_change >= .40:
            img8 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown3.png')))
            Label.image = img8

        elif .40 > percent_change >= .20:
            img9 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown4.png')))
            Label.configure(image=img9)
            Label.image = img9

        elif .20 > percent_change >= .5:
            img10 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown5.png')))
            Label.configure(image=img10)
            Label.image = img10

        elif .5 > percent_change:
            img11 = ImageTk.PhotoImage(Image.open(path.join('images', 'clown6.png')))
            Label.configure(image=img11)
            Label.image = img11

    return Label.image


class Coin:
    def __init__(self, name, numbought, buyprice, image):
        self.name = name
        self.numbought = numbought
        self.buyprice = buyprice
        self.image= image

    def get_name(self):
        return self.name

    def get_numbought(self):
        return self.numbought

    def get_buyprice(self):
        return self.buyprice


bitcoinval = 50000

given_data = [{"cryptoname": "bitcoin", "coinsbought": 1, "buyprice": 500, "currentprice": 10000}]

for item in given_data:
    name = item["cryptoname"]
    numbought = item["coinsbought"]
    buyprice = item["currentprice"]
    main_img = memeify()

    item["cryptoname"] = Coin(name, numbought, buyprice, main_img)



# Update the meme. calling the memeify method
make_frame = LabelFrame(root, text="Sample Image", width=100, height=100)
make_frame.pack()


foo = ImageTk.PhotoImage(Image.open(path.join('images', 'wrestler1.png')))

def testwindow():
    foo_testLabel = Label(root, image=foo)
    foo_testLabel.pack()

testwindow()
root.mainloop()