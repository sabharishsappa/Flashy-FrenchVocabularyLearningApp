
from tkinter import *
import pandas as pd
import random
import time


# Global variables
BACKGROUND_COLOR = "#B1DDC6"
current_word={}
dict_data={}

# Data Import
try :
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    dict_data = original_data.to_dict(orient="records")


else:
    dict_data = data.to_dict(orient="records")

def next_card():

    global current_word, flip_timer

    n = len(dict_data)
    if(n>0):
        window.after_cancel(flip_timer)
        current_word = random.choice(dict_data)
        canvas.itemconfig(card_title_text,text="French",fill="black")
        canvas.itemconfig(card_word_text,text=current_word["French"],fill="black")
        canvas.itemconfig(card_background,image=card_frnt_image)
        flip_timer = window.after(3000,func=flip_card)


    else:
        print("No More Words to learn...")

def handle_known():
    global current_word

    dict_data.remove(current_word)
    data = pd.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def handle_unknown():
    next_card()
    
def flip_card():
    canvas.itemconfig(card_background,image=card_back_image)
    canvas.itemconfig(card_title_text,text="English",fill="white")
    canvas.itemconfig(card_word_text,text=current_word["English"],fill="white")





#-----------------------------------UI Setup-----------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

#Canvas

canvas = Canvas(width=800,height=526)
card_frnt_image = PhotoImage(file="images/card_front.png")
card_back_image= PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400,263,image=card_frnt_image)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
card_title_text = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"),fill="black")
card_word_text = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"),fill="black")
canvas.grid(row=0,column=0,columnspan=2)

#buttons
right_btn_image = PhotoImage(file="images/right.png")
wrong_btn_image = PhotoImage(file="images/wrong.png")
right_btn = Button(image=right_btn_image,highlightthickness=0,command=handle_known)
right_btn.grid(row=1,column=1)
wrong_btn = Button(image=wrong_btn_image,highlightthickness=0,command=handle_unknown)
wrong_btn.grid(row=1,column=0)


next_card()

window.mainloop()