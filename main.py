import numbers
from tkinter import *
from numpy import *
import operatorFunctions as op

#Window Initialization
root = Tk() 
root.title("Calculator")
root.geometry("300x300")

#Frame Initialization
frame = Frame(root) 
frame.pack()

#Global Variables Initialization
equation = []
expression = StringVar()

# Operators for simple calculation
operators = [ 
    { "value": "+", "text": '+' },
    { "value": "-", "text": '-' },
    { "value": "*", "text": 'x' },
    { "value": "/", "text": '÷' },
    { "value": ".", "text": '.' },
    { "value": "(", "text": '(' },
    { "value": ")", "text": ')' },
]
functionalOperators = ["clear", "<-"]

# Functions
objects = op.operators(frame, equation, expression) #All functions from operatorFunctions.py are now in buttonCommands
expression.trace("w", lambda name, index, mode, sv=expression: objects.updateHandler())

# Input Field Initialization
inputField = Entry(frame, textvariable=expression)
inputField.grid(row=0, column=0, columnspan=5)
inputField.justify = RIGHT

#Button List (Stores the array of buttons inside (Testing Purposes))
buttonList = []

row = 2 # Just a global row variable to keep track of the row

# For Loop to create Num Pad Buttons
for num in range(1,11):
    if num == 10:
       objects.buttons(0, '0').grid(row=row+3, column=2)
       buttonList.append(objects.buttons(0, 0))
    else:
        objects.buttons(num, str(num)).grid(row=row + ((num-1)//3), column=1+((num - 1)%3))
        buttonList.append(objects.buttons(num, num))

# For Loop to create Operator Buttons
for ops in operators:
    if ops["value"] == ".":
        objects.buttons(".", ".").grid(row=row + 3, column=1)
        buttonList.append(objects.buttons(".", "."))
    elif ops["value"] == "(":
        objects.buttons("(", "(").grid(row=row - 1, column=2)
        buttonList.append(objects.buttons("(", "("))
    elif ops["value"] == ")":
        objects.buttons(")", ")").grid(row=row - 1, column=3)
        buttonList.append(objects.buttons(")", ")"))
    else:
        objects.buttons(ops["text"], ops["value"]).grid(row=row + operators.index(ops), column=4)
        buttonList.append(objects.buttons(ops["text"], ops["value"]))

# For Loop to create Functional Operator Buttons
for i in functionalOperators:
    if i == "clear":
        Button(frame, text=i, command=lambda: objects.clear()).grid(row=row+4, column=1, columnspan=3)
    elif i == "<-":
        Button(frame, text=i, command=lambda: objects.delete()).grid(row=row+4, column=0)
    

#Equal Button
equalButton = Button(frame, text="=", command=lambda: objects.solve())
equalButton.grid(row=row + 3, column=3)
 
root.mainloop() #Finalize the window