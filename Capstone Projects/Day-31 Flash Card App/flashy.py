from tkinter import *
import pandas as pd
import random
import os
BACKGROUND_COLOR = "#B1DDC6"

# Change the current working directory to the Script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the data
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/words_data.csv")
    to_learn = original_data.to_dict(orient="records")
    print("opening Original words file")
else:
    to_learn = data.to_dict(orient="records")
    print("opening words to learn file")
current_card = {}
# #------------------------------------NEXT CARD---------------------------------#
def next_card():
    global current_card,flip_timer
    try:
        window.after_cancel(flip_timer)
    except NameError:
        pass
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_tittle,text = "French",fill="black")
    canvas.itemconfig(card_word,text = current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
#------------------------------------FLIP CARD---------------------------------#
def flip_card():
    canvas.itemconfig(card_tittle,text = "English",fill="blue")
    canvas.itemconfig(card_word,text = current_card["English"],fill="blue")
    canvas.itemconfig(card_background, image=card_back_img)

#------------------------------------is_known---------------------------------#
def is_known():
    global to_learn
    if current_card in to_learn:
        to_learn.remove(current_card)
    else:
        print(f"Error: {current_card} not found in to_learn list.")
    # to_learn.remove(current_card)
    # print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)

    next_card()

#------------------------------------UI SETUP---------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file = "images/front.png")
card_back_img = PhotoImage(file = "images/back.png")

card_background = canvas.create_image(400,263,image = card_front_img)
card_tittle = canvas.create_text(400,150,text="Tittle",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/false_button.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=flip_card)
unknown_button.grid(row=1,column=0)

tick_image = PhotoImage(file="images/true_button.png")
known_button = Button(image=tick_image, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

window.mainloop()
