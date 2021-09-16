from tkinter import *
from PIL import ImageTk, Image
import os

imgfolderpath = "MLimages"
filelist = os.listdir(imgfolderpath) # dir is your directory path
numberfiles = len(filelist )
# print(number_files)

path = r"iconfile.ico"

# Users interface objects
root = Tk()
root.title("Machine Learning is the future")
root.iconbitmap(path)

# Functions on-click
def exit():
    root.quit()

def myfuncback(imagenumber):
    global mylabel
    global buttonforward
    global buttonback

    mylabel.grid_forget()

    mylabel = Label(image=myimglist[imagenumber-1])
    buttonback = Button(root, text="<<",
                        command=lambda: myfuncback(imagenumber-1))
    buttonforward = Button(root, text=">>",
                           command=lambda: myfuncforward(imagenumber+1))

    if imagenumber == 1:
        buttonback = Button(root, text="<<", state=DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    buttonback.grid(row=1, column=0)
    buttonforward.grid(row=1, column=2)

    global mystatus
    mystatus = Label(root, text="Image " + str(imagenumber) + " of " + str(len(myimglist)),
                     bd=2, relief=SUNKEN, anchor=E)  # East
    mystatus.grid(row=2, column=0, columnspan=3, sticky=W + E)  # East and We


def myfuncforward(imagenumber):
    global mylabel
    global buttonforward
    global buttonback
    global numberfiles

    mylabel.grid_forget()

    mylabel = Label(image=myimglist[imagenumber-1])
    buttonback = Button(root, text="<<",
                        command=lambda: myfuncback(imagenumber-1))
    buttonforward = Button(root, text=">>",
                           command=lambda: myfuncforward(imagenumber+1))

    if imagenumber == numberfiles:
        buttonforward = Button(root, text=">>", state=DISABLED)

    mylabel.grid(row=0, column=0, columnspan=3)
    buttonback.grid(row=1, column=0)
    buttonforward.grid(row=1, column=2)

    global mystatus
    mystatus = Label(root, text="Image " + str(imagenumber) + " of " + str(len(myimglist)),
                     bd=2, relief=SUNKEN, anchor=E)  # East
    mystatus.grid(row=2, column=0, columnspan=3, sticky=W + E)  # East and West

#Button widgets (Initial Condition)
buttonback = Button(root, text="<<", command= myfuncback, state=DISABLED)
buttonquit = Button(root, text="Exit Program", command=exit)
buttonforward = Button(root, text=">>", command=lambda: myfuncforward(2))

#Images widgets
myimg1 = ImageTk.PhotoImage(Image.open("MLimages/MLimg1.jpg"))
myimg2 = ImageTk.PhotoImage(Image.open("MLimages/MLimg2.jpg"))
myimg3 = ImageTk.PhotoImage(Image.open("MLimages/MLimg3.jpg"))
myimg4 = ImageTk.PhotoImage(Image.open("MLimages/MLimg4.jpg"))
myimg5 = ImageTk.PhotoImage(Image.open("MLimages/MLimg5.jpg"))
myimg6 = ImageTk.PhotoImage(Image.open("MLimages/MLimg6.jpg"))

myimglist = [myimg1, myimg2, myimg3, myimg4, myimg5, myimg6]

mystatus = Label(root, text="Image "+ str(1) + " of " + str(len(myimglist)),
                 bd=2, relief=SUNKEN, anchor=E) # East

mylabel = Label(image=myimg1)
mylabel.grid(row=0, column=0, columnspan=3)

# Showing buttons
buttonback.grid(row=1, column=0)
buttonquit.grid(row=1, column=1, pady=15)
buttonforward.grid(row=1, column=2)
mystatus.grid(row=2, column=0, columnspan=3, sticky=W+E) # East and West

# Everything in the motion is a loop
root.mainloop()

