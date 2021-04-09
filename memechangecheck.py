from tkinter import *
from PIL import ImageTk, Image
root=Tk()
img = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler1.png'))
panel = Label(root, image=img)
panel.pack(side="right", fill="both", expand="no")

#pur_coin_amt = amount of coin that was purchased entered by user and stored in database
#pur_coin_val = price that owner paid entered by user and stored in database
#act_coin_val = current price of 1 coin. gotten from other file, needs to be updated on some time scale
#sell_factor
#buy_factor
def determine_picture(pur_coin_amt, pur_coin_val, act_coin_val):

    if pur_coin_amt * act_coin_val != pur_coin_val:

        if pur_coin_amt * act_coin_val >= pur_coin_val * 2: #if current amt is equal to or greater than 100% of buying price
            img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler5.png'))
            panel.configure(image=img1)
            panel.image = img1

        elif pur_coin_val * 2 > pur_coin_amt * act_coin_val >= pur_coin_val * 1.75:
            img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler4.png'))
            panel.configure(image=img2)
            panel.image = img2

        elif pur_coin_val * 1.75 > pur_coin_amt * act_coin_val >= pur_coin_val * 1.50:
            img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler3.png'))
            panel.configure(image=img3)
            panel.image = img3

        elif pur_coin_val * 1.50 > pur_coin_amt * act_coin_val >= pur_coin_val * 1.25:
            img4 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler2.png'))
            panel.configure(image=img4)
            panel.image = img4

        elif pur_coin_val * 1.25 > pur_coin_amt * act_coin_val > pur_coin_val:
            img5 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\wrestler1.png'))
            panel.configure(image=img5)
            panel.image = img5

        elif pur_coin_val > pur_coin_amt * act_coin_val >= pur_coin_val * .80:
            img6 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown1.png'))
            panel.configure(image=img6)
            panel.image = img6

        elif pur_coin_val * .80 > pur_coin_amt * act_coin_val >= pur_coin_val * .60:
            img7 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown2.png'))
            panel.configure(image=img7)
            panel.image = img7

        elif pur_coin_val * .60 > pur_coin_amt * act_coin_val >= pur_coin_val * .40:
            img8 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown3.png'))
            panel.configure(image=img8)
            panel.image = img8

        elif pur_coin_val * .40 > pur_coin_amt * act_coin_val >= pur_coin_val * .20:
            img9 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown4.png'))
            panel.configure(image=img9)
            panel.image = img9

        elif pur_coin_val * .20 > pur_coin_amt * act_coin_val >= pur_coin_val * .5:
            img10 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown5.png'))
            panel.configure(image=img10)
            panel.image = img10

        elif pur_coin_val * .5 > pur_coin_amt * act_coin_val:
            img11 = ImageTk.PhotoImage(Image.open(r'C:\Users\alexa\PycharmProjects\hackathon\images\clown6.png'))
            panel.configure(image=img11)
            panel.image = img11

    elif pur_coin_amt * act_coin_val == pur_coin_val:
        #return "no change" image?"""
        print("same")

#root.bind("<Return>", determine_picture(1, , 100))
determine_picture(1, 170, 100)
root.mainloop()