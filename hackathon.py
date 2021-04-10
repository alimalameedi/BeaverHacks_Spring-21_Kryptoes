from tkinter import*
import sqlite3
import EnterCrypto

# create a database
conn = sqlite3.connect("Wallet.db")

# create cursor
c = conn.cursor()

# insert into table
try:
    c.execute("""CREATE TABLE wallet (
              cryptocurrency text,
              quantity float,
              price float
              )
              """)
except:
    print()

def query():
    """ Print out the amount BTC bought """
    # open database and set cursor
    conn = sqlite3.connect("Wallet.db")
    c = conn.cursor()

    # print out records
    c.execute("SELECT *, oid FROM wallet")
    records.var = c.fetchall()

    print(records.var)

    entries = c.execute("SELECT COUNT() FROM wallet")

    print(entries.fetchone()[0])

    bitcoins = c.execute("SELECT cryptocurrency FROM wallet wherer cryptocurrency='Bitcoin")
    bitcoins = c.fetchall()
    print(bitcoins)

    conn.close()

def return_records():
    return records.var

# root window
root = Tk()
root.title("Our App")
root.geometry("400x400")

# Enter BTC value window
enterButton = Button(root, text="New Crypto", command = EnterCrypto.enterNewCrypto)
enterButton.grid(row=0, column=0)

# query
query_btn = Button(root, text="Show Record", command = query)
query_btn.grid(row=1, column=0)

# Create app
root.mainloop()

