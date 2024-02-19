#1. Random
# import random 
from random import random 
# Prints random item 
print(random())
print("\n")

#2.Random using List
# import random 
import random 
# prints a random value from the list 
list1 = [1, 2, 3, 4, 5, 6] 
print(random.choice(list1))
print("\n")

#3.Random using List
import random 
random.seed(5) 
print(random.random()) 
print(random.random())
print("\n")

#4. Random number
#import random 
# Generates a random number between 
# a given positive range 
r1 = random.randint(5, 15) 
print("Random number between 5 and 15 is % s" % (r1)) 
# Generates a random number between

# two given negative range 
r2 = random.randint(-10, -2) 
print("Random number between -10 and -2 is % d" % (r2))
print("\n")

#5.Message Box
from tkinter import * 
from tkinter import messagebox 

root = Tk() 
root.geometry("300x200") 
w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 
messagebox.showinfo("showinfo", "Information") 
messagebox.showwarning("showwarning", "Warning") 
messagebox.showerror("showerror", "Error") 
messagebox.askquestion("askquestion", "Are you sure?") 
messagebox.askokcancel("askokcancel", "Want to continue?") 
messagebox.askyesno("askyesno", "Find the value?") 
messagebox.askretrycancel("askretrycancel", "Try again?") 
root.mainloop()
print("\n")

#6. Menu Button
from tkinter import * 
from tkinter import messagebox 
top = Tk() 
mb= Menubutton ( top, text="Course", relief=RAISED ) 
mb.grid() 
mb.menu = Menu ( mb, tearoff = 0 ) 
mb["menu"] = mb.menu 
pythonVar = IntVar() 
javaVar = IntVar() 
mb.menu.add_checkbutton ( label="Python", variable=pythonVar ) 
mb.menu.add_checkbutton ( label="Java", variable=javaVar ) 
mb.pack() 
top.mainloop()
print("\n")

#7. Radio Button
from tkinter import * 
def sel(): 
    selection = "You selected the option " + str(var.get()) 
    label.config(text = selection) 
root = Tk() 
var = IntVar() 
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel) 
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel) 
R2.pack( anchor = W ) 
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel) 
R3.pack( anchor = W) 
label = Label(root) 
label.pack() 
root.mainloop()
print("\n")

#8. Message
import tkinter as tk 
mast = tk.Tk() 
whatever_you_do = "Welcome to Python Course.\n(Univ. Kuala Lumpur)" 
msg = tk.Message(mast, text = whatever_you_do) 
msg.config(bg='lightgreen', font=('times', 24, 'italic')) 
msg.pack() 
tk.mainloop()
print("\n")

#9. Convert feet to meter
from tkinter import * 
from tkinter import ttk 
def calculate(*args): 
    try: 
        value = float(feet.get()) 
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0) 
    except ValueError: 
        pass
root = Tk() # create GUI application (root) 
root.title("Feet to Meters") 
mainframe = ttk.Frame(root, padding="3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) 
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1) 
feet = StringVar() 
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) 
feet_entry.grid(column=2, row=1, sticky=(W, E)) 
meters = StringVar() 
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) 
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W) 
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) 
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E) 
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W) 
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5) 
feet_entry.focus() 
root.bind("<Return>", calculate)
root.mainloop()
print("\n")

#10. Calculator
# Python program to create a simple GUI 
# calculator using Tkinter 
#import everything from tkinter module 
from tkinter import * 
# globally declare the expression variable 
expression = "" 

# Function to update expression 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
    
    # concatenation of string 
    expression = expression + str(num) 
    
    # update the expression by using set method 
    equation.set(expression) 
    
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
    # Put that code inside the try block 
    # which may generate the error 
    try: 
        global expression
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
        equation.set(total) 
        # initialize the expression variable 
        # by empty string 
        expression = "" 
        # if error is generate then handle 
        # by the except block 
    except: 
        equation.set(" error ") 
        expression = "" 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
    
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
    
    # set the background colour of GUI window 
    gui.configure(background="light green") 
    # set the title of GUI window 
    gui.title("Simple Calculator")
    # set the configuration of GUI window
    gui.geometry("270x150") 
    
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 
    
    # grid method is used for placing 
    # the widgets at respective positions
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='lightblue', command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
    button2 = Button(gui, text=' 2 ', fg='black', bg='lightblue', command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
    button3 = Button(gui, text=' 3 ', fg='black', bg='lightblue', command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
    button4 = Button(gui, text=' 4 ',fg='black', bg='lightblue', command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
    button5 = Button(gui, text=' 5 ', fg='black', bg='lightblue', command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
    button6 = Button(gui, text=' 6 ', fg='black', bg='lightblue', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2) 
    button7 = Button(gui, text=' 7 ', fg='black', bg='lightblue', command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
    button8 = Button(gui, text=' 8 ', fg='black', bg='lightblue', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
    button9 = Button(gui, text=' 9 ', fg='black', bg='lightblue', command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
    button0 = Button(gui, text=' 0 ', fg='black', bg='lightblue', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
    plus = Button(gui, text=' + ', fg='black', bg='lightblue', command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3) 
minus = Button(gui, text=' - ', fg='black', bg='lightblue', command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3)
multiply = Button(gui, text=' * ', fg='black', bg='lightblue', command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 
divide = Button(gui, text=' / ', fg='black', bg='lightblue', command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 
equal = Button(gui, text=' = ', fg='black', bg='lightblue', command=equalpress, height=1, width=7) 
equal.grid(row=5, column=2) 
clear = Button(gui, text='Clear', fg='black', bg='lightblue', command=clear, height=1, width=7) 
clear.grid(row=5, column='1') 
Decimal= Button(gui, text='.', fg='black', bg='lightblue', command=lambda: press('.'), height=1, width=7) 
Decimal.grid(row=6, column=0) # start the GUI gui.mainloop()
print("\n")


#1 using tkinter
import tkinter as tk

def calculate_perimeter():
    length = float(entry_length.get())
    width = float(entry_width.get())
    perimeter = 2 * length + 2 * width
    label_result.config(text=f"Perimeter: {perimeter}")

def calculate_area():
    length = float(entry_length.get())
    width = float(entry_width.get())
    area = length * width
    label_result.config(text=f"Area: {area}")

# Create the main window
root = tk.Tk()
root.title("Rectangle Calculator")

# Create labels and entry widgets
label_length = tk.Label(root, text="Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

label_width = tk.Label(root, text="Width:")
label_width.grid(row=1, column=0, padx=10, pady=10)

entry_width = tk.Entry(root)
entry_width.grid(row=1, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Create buttons for calculations
button_perimeter = tk.Button(root, text="Calculate Perimeter", command=calculate_perimeter)
button_perimeter.grid(row=3, column=0, columnspan=2, pady=10)

button_area = tk.Button(root, text="Calculate Area", command=calculate_area)
button_area.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
print("\n")
