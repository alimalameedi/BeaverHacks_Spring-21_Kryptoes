import sqlite3
import getapi

value = getapi.bitcoin_api()

def get_priceAndQuantity(cryptocurrency):
    """
    Gets the price and quantity of the cryptocurrecy user purchased

    :param cryptocurrency: the name of the cryptocurrency
    :return: Tuple containing the quantity and price (quantity, price)
    """

    # connect to database
    conn = sqlite3.connect("Wallet.db")

    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM wallet WHERE cryptocurrency='%s'" %cryptocurrency)

    values = c.fetchall()

    # commit and close
    conn.commit()
    conn.close()

    return (values[0][1],values[0][2])