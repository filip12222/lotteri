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

def update_listbox(antal_lotter):
    #tömmer listboxen
    Listbox.delete(0, END)
    # Lägger till text
    Listbox.insert(1, "Grattis du van detta!")

    try:
        int_antal_lotter = int(antal_lotter)
        i=0

    
        if (int_antal_lotter < 4):

            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                Listbox.insert((i+2), vinst)
                i += 1

        elif (int_antal_lotter < 3):
            messagebox.showinfo("du har valt för många lotter")

    except ValueError:
        messagebox.showinfo("Endast sifftor tillåtna")

def ClickSlumpButton():    
#print("tryck")
    antal_lott = Textbox_antal.get()
    print(f"tryck1 {antal_lott}")
    print("vanlig print tryck!")


    #tömmer listbox
    Textbox_antal.delete(0, END)
    #sätter fokus på förste entryt
    Textbox_antal.focus_set()
    update_listbox(antal_lott)


#skapar knapp
Button_slumpa = Button(text="TUR KNAPP!", command=ClickSlumpButton)
Button_slumpa.grid(row=1, column=0, sticky=E, padx=15, pady=15)

Listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()