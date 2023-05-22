from tkinter import *
from tkinter import messagebox
import lotteri

# create root window
root = Tk()
root.title("Lotteri") 

#create listbox
Listbox = Listbox(root, height=4,
                  width=30,
                  bg="white", 
                  activestyle="dotbox",
                  font="halvetica",
                  fg="blue")


#definerar storlek på fönster
root.geometry("300x300")

lotteriet = lotteri.lotteri()

#skapar label
Label_antal = Label(root, text="Antal lotter, max 3st: ")
Label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)

# skapas textfält
Textbox_antal = Entry(root, width=2) 
Textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
Textbox_antal.focus_set()

def ClickSlumpButton()
print("tryck!")

#skapar knapp
Button_slumpa = Button(text="TUR KNAPP!", command=ClickSlumpButton)
Button_slumpa.grid(row=2, column=0, sticky=E, padx=15, pady=15)


root.mainloop()