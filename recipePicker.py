import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random


bg_color = "#3d6466"

def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    #choosing random number for grabbing recipe
    idx = random.randint(0, len(all_tables)-1)

    #grab ingredients
    table_name = all_tables[idx][1]
    #grabbing all the ingredients for the random recipe
    cursor.execute("SELECT * FROM " + table_name + ";")
    #storing all the data we grabbed above
    ingredients = cursor.fetchall()

    print(ingredients)
    print(table_name)
    connection.close()

def laod_frame1():
    #this makes sure the background color stays with the logo on screen
    frame1.pack_propagate(False)
    #widgets for frame1
    logo_image = ImageTk.PhotoImage(file = "assets/RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image = logo_image, bg = bg_color)
    logo_widget.image = logo_image
    logo_widget.pack(padx=10, pady=10)


    tk.Label(frame1, text = "ready for your random recipe?", 
                        bg = bg_color, 
                        fg = "white",
                        font = ("TkMenuFont", 14)
                        ).pack(padx=10, pady=10)

    tk.Button(
        frame1,
        text = "SHUFFLE",
        font = ("TkHeadingFont", 20),
        bg = "#28393a",
        fg = "white",
        cursor = "hand2",
        activebackground = "#badee2",
        activeforeground = 'black',
        command = load_frame2
    ).pack(padx=20, pady=10)


def load_frame2():
    fetch_db()




# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
#places window at the center of the screen
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x)+'+' + str(y))

#frame widget
frame1 = tk.Frame(root, width = 500, height = 600, bg = bg_color)
frame2 = tk.Frame(root,  bg = bg_color)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

laod_frame1()


# run app
root.mainloop()