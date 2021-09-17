from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe Games")
root.iconbitmap('tictactoe.ico')

# X turns when true
# O turns when false
clicked = True
count = 0

def myfuncclick(mybutton):
    global clicked, count
    if mybutton["text"] == " " and clicked == True:
        mybutton["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif mybutton["text"] == " " and clicked == False:
        mybutton["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe Rules", "It was chosen")

def disableallbutton():
    mybutton1.config(state=DISABLED)
    mybutton2.config(state=DISABLED)
    mybutton3.config(state=DISABLED)
    mybutton4.config(state=DISABLED)
    mybutton5.config(state=DISABLED)
    mybutton6.config(state=DISABLED)
    mybutton7.config(state=DISABLED)
    mybutton8.config(state=DISABLED)
    mybutton9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False
    xmark = "X"
    omark = "O"
    if mybutton1["text"] == xmark and mybutton2["text"] == xmark and mybutton3["text"] == xmark:
        mybutton1.config(bg="red")
        mybutton2.config(bg="red")
        mybutton3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()
    elif mybutton4["text"] == xmark and mybutton5["text"] == xmark and mybutton6["text"] == xmark:
        mybutton4.config(bg="red")
        mybutton5.config(bg="red")
        mybutton6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()
    elif mybutton7["text"] == xmark and mybutton8["text"] == xmark and mybutton9["text"] == xmark:
        mybutton7.config(bg="red")
        mybutton8.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()
    elif mybutton1["text"] == xmark and mybutton4["text"] == xmark and mybutton7["text"] == xmark:
        mybutton1.config(bg="red")
        mybutton4.config(bg="red")
        mybutton7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()
    elif mybutton2["text"] == xmark and mybutton5["text"] == xmark and mybutton8["text"] == xmark:
        mybutton2.config(bg="red")
        mybutton5.config(bg="red")
        mybutton8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()
    elif mybutton3["text"] == xmark and mybutton6["text"] == xmark and mybutton9["text"] == xmark:
        mybutton3.config(bg="red")
        mybutton6.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()

    elif mybutton1["text"] == xmark and mybutton5["text"] == xmark and mybutton9["text"] == xmark:
        mybutton1.config(bg="red")
        mybutton5.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()

    elif mybutton3["text"] == xmark and mybutton5["text"] == xmark and mybutton7["text"] == xmark:
        mybutton3.config(bg="red")
        mybutton5.config(bg="red")
        mybutton7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is X")
        disableallbutton()

    # Check if O win
    elif mybutton1["text"] == omark and mybutton2["text"] == omark and mybutton3["text"] == omark:
        mybutton1.config(bg="red")
        mybutton2.config(bg="red")
        mybutton3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()
    elif mybutton4["text"] == omark and mybutton5["text"] == omark and mybutton6["text"] == omark:
        mybutton4.config(bg="red")
        mybutton5.config(bg="red")
        mybutton6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()
    elif mybutton7["text"] == omark and mybutton8["text"] == omark and mybutton9["text"] == omark:
        mybutton7.config(bg="red")
        mybutton8.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()
    elif mybutton1["text"] == omark and mybutton4["text"] == omark and mybutton7["text"] == omark:
        mybutton1.config(bg="red")
        mybutton4.config(bg="red")
        mybutton7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()
    elif mybutton2["text"] == omark and mybutton5["text"] == omark and mybutton8["text"] == omark:
        mybutton2.config(bg="red")
        mybutton5.config(bg="red")
        mybutton8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()
    elif mybutton3["text"] == omark and mybutton6["text"] == omark and mybutton9["text"] == omark:
        mybutton3.config(bg="red")
        mybutton6.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()

    elif mybutton1["text"] == omark and mybutton5["text"] == omark and mybutton9["text"] == omark:
        mybutton1.config(bg="red")
        mybutton5.config(bg="red")
        mybutton9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()

    elif mybutton3["text"] == omark and mybutton5["text"] == omark and mybutton7["text"] == omark:
        mybutton3.config(bg="red")
        mybutton5.config(bg="red")
        mybutton7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe Rule", "Winner is O")
        disableallbutton()

    elif count ==9 and winner == False:
        messagebox.showinfo("Tic Tac Toe Rules", "It is a draw")
        disableallbutton()

# Building buttons
mybutton1 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton1))
mybutton2 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton2))
mybutton3 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton3))
mybutton4 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton4))
mybutton5 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton5))
mybutton6 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton6))
mybutton7 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton7))
mybutton8 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton8))
mybutton9 = Button(root, text=" ", font=("Arial", 20), bg="blue", height = 4, width = 7,
                   command=lambda: myfuncclick(mybutton9))

mybutton1.grid(row=0, column=0)
mybutton2.grid(row=0, column=1)
mybutton3.grid(row=0, column=2)

mybutton4.grid(row=1, column=0)
mybutton5.grid(row=1, column=1)
mybutton6.grid(row=1, column=2)

mybutton7.grid(row=2, column=0)
mybutton8.grid(row=2, column=1)
mybutton9.grid(row=2, column=2)

# Everything in the motion is a loop
root.mainloop()