from tkinter import *
# import subprocess
import math as mathlib

# Users interface objects
root = Tk()
root.title("Simple Calculator")
# Functions when clicking buttons
def buttonfuncclick(number):
    # myentry.delete(0, END)
    currentval = myentry.get()
    myentry.delete(0, END)
    myentry.insert(0, str(currentval) + str(number))


def buttonfuncdot():
    currentval = myentry.get()
    myentry.delete(0, END)
    myentry.insert(0, str(currentval) + ".")

def buttonfuncexp():
    # firstnumber = myentry.get()
    # global firstnum
    # if firstnumber.isdigit() or "." in firstnumber:
    #     firstnum = float(firstnumber)
    # else:
    #     firstnum = 0
    # myentry.delete(0, END)
    myentry.insert(0, "e")

def buttonfuncclear():
    myentry.delete(0, END)

def buttonfuncadd():
    firstnumber = myentry.get()
    if "e" in firstnumber:
        tempnum = firstnumber.replace("e", "")
        tempnum = float(tempnum)
        firstnumber = mathlib.exp(tempnum)
        firstnumber = str(firstnumber)
    global firstnum
    global math
    math = "addition"
    if firstnumber.isdigit() or "." in firstnumber:
        firstnum = float(firstnumber)
    else:
        firstnum = 0
    myentry.delete(0,END)

def buttonfuncminus():
    firstnumber = myentry.get()
    global firstnum
    global math
    math = "subtraction"
    if firstnumber.isdigit() or "." in firstnumber:
        firstnum = float(firstnumber)
    else:
        firstnum = 0
    myentry.delete(0,END)

def buttonfuncmul():
    firstnumber = myentry.get()
    global firstnum
    global math
    math = "multiplication"
    if firstnumber.isdigit() or "." in firstnumber:
        firstnum = float(firstnumber)
    else:
        firstnum = 0
    myentry.delete(0,END)

def buttonfuncdiv():
    firstnumber = myentry.get()
    global firstnum
    global math
    math = "division"
    if firstnumber.isdigit() or "." in firstnumber:
        firstnum = float(firstnumber)
    else:
        firstnum = 0
    myentry.delete(0,END)

def buttonfuncmodulus():
    firstnumber = myentry.get()
    global firstnum
    global math
    math = "modulus"
    if firstnumber.isdigit() or "." in firstnumber:
        firstnum = float(firstnumber)
    else:
        firstnum = 0
    myentry.delete(0,END)


def buttonfuncequal():
    secondnumber = myentry.get()
    myentry.delete(0,END)
    if "e" in secondnumber:
        tempnum = secondnumber.replace("e", "")
        tempnum = float(tempnum)
        secondnumber = mathlib.exp(tempnum)
        if firstnum == 0:
            myentry.insert(0, secondnumber)
            global math
            math = ""

    if math == "addition":
        myentry.insert(0, firstnum + float(secondnumber))
    elif math == "subtraction":
        myentry.insert(0, firstnum - float(secondnumber))
    elif math== "multiplication":
        myentry.insert(0, firstnum * float(secondnumber))
    elif math == "division":
        myentry.insert(0, firstnum / float(secondnumber))
    elif math == "modulus":
        myentry.insert(0, firstnum % float(secondnumber))





# Entry widgets
myentry = Entry(root, width=50, fg="white", bg="black",
                borderwidth=10)
myentry.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
# myentry.insert(2, "Enter your ID: ")

# Creating button widget
xwidth = 30
ywidth = 10
mybutton1 = Button(root, text="1", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(1), fg="white", bg="black")
mybutton2 = Button(root, text="2", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(2), fg="white", bg="black")
mybutton3 = Button(root, text="3", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(3), fg="white", bg="black")
mybutton4 = Button(root, text="4", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(4), fg="white", bg="black")
mybutton5 = Button(root, text="5", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(5), fg="white", bg="black")
mybutton6 = Button(root, text="6", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(6), fg="white", bg="black")
mybutton7 = Button(root, text="7", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(7), fg="white", bg="black")
mybutton8 = Button(root, text="8", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(8), fg="white", bg="black")
mybutton9 = Button(root, text="9", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(9), fg="white", bg="black")
mybutton0 = Button(root, text="0", padx=xwidth, pady=ywidth,
                  command=lambda: buttonfuncclick(0), fg="white", bg="black")
mybuttonclear = Button(root, text="Clear", padx=60, pady=ywidth,
                  command= buttonfuncclear, fg="white", bg="black")
mybuttonadd = Button(root, text="+", padx=xwidth, pady=ywidth,
                  command=buttonfuncadd, fg="white", bg="black")
mybuttonminus = Button(root, text="-", padx=xwidth, pady=ywidth,
                  command=buttonfuncminus, fg="white", bg="black")
mybuttonmul = Button(root, text="*", padx=xwidth, pady=ywidth,
                  command=buttonfuncmul, fg="white", bg="black")
mybuttondiv = Button(root, text="/", padx=xwidth, pady=ywidth,
                  command=buttonfuncdiv, fg="white", bg="black")
mybuttonequal = Button(root, text="=", padx=xwidth, pady=ywidth,
                  command=buttonfuncequal, fg="white", bg="black")
mybuttondot = Button(root, text=".", padx=xwidth, pady=ywidth,
                  command=buttonfuncdot, fg="white", bg="black")
mybuttonexp = Button(root, text="e", padx=xwidth, pady=ywidth,
                  command=buttonfuncexp, fg="white", bg="black")
mybuttonmodulus = Button(root, text="%", padx=xwidth, pady=ywidth,
                  command=buttonfuncmodulus, fg="white", bg="black")

# Showing on the screen
mybutton1.grid(row=2, column=0)
mybutton2.grid(row=2, column=1)
mybutton3.grid(row=2, column=2)
mybuttonminus.grid(row=2, column=3)

mybutton4.grid(row=3, column=0)
mybutton5.grid(row=3, column=1)
mybutton6.grid(row=3, column=2)
mybuttonmul.grid(row=3, column=3)

mybutton7.grid(row=4, column=0)
mybutton8.grid(row=4, column=1)
mybutton9.grid(row=4, column=2)
mybuttondiv.grid(row=4, column=3)

mybuttonequal.grid(row=5, column=0)
mybuttondot.grid(row=5, column=1)
mybuttonexp.grid(row=5, column=2)
mybuttonmodulus.grid(row=5, column=3)

mybutton0.grid(row=1, column=0)
mybuttonclear.grid(row=1, column=1, columnspan=2)
mybuttonadd.grid(row=1, column=3)
# Everything in the motion is a loop
root.mainloop()








