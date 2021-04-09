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
    records = c.fetchall()
    print(records)

    # commit and close
    conn.commit()
    conn.close()

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

