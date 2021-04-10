from tkinter import*
import sqlite3

def enterNewCrypto():
    """
    Opens a new window where user can input the quantity of BTC they own

    """
    global cryptoNameEntryLabel
    global cryptoName
    global quantityLabel
    global quantity
    global price

    top = Toplevel()
    top.geometry("200x100")

    # Enter Crypto name
    cryptoNameEntryLabel = Label(top, text= "Cryptocurrency: ")
    cryptoName = Entry(top)

    # Enter the quantity of crypto
    quantityLabel = Label(top, text="Quantity: ")
    quantity = Entry(top)

    # Enter buying price
    priceLabel = Label(top, text="Price: ")
    price = Entry(top)

    # submit value and place into db file via SQLite
    submit_button = Button(top, text="Save", command =lambda: submitAndQuit(top))

    # cancel entry
    cancel_button = Button(top, text="Cancel", command = top.destroy)

    # formatting
    cryptoNameEntryLabel.grid(row=0, column=0)
    cryptoName.grid(row=0, column=1)

    quantityLabel.grid(row=1, column=0)
    quantity.grid(row=1, column=1)


    priceLabel.grid(row=2, column=0)
    price.grid(row=2, column =1)

    submit_button.grid(row=3, column=0)
    cancel_button.grid(row=3, column=1)

def submitAndQuit(window):
    submit()
    window.destroy()

def submit():
    # create a database
    conn = sqlite3.connect("Wallet.db")

    # create cursor
    c = conn.cursor()

    # insert into table

    c.execute("INSERT INTO wallet VALUES (:cryptocurrency, :quantity, :price)",
              {
                  "cryptocurrency": cryptoName.get(),
                  "quantity": quantity.get(),
                  "price": price.get()
              })

    conn.commit()
    conn.close()

    # clear text box
    quantity.delete(0,END)