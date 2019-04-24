import tkinter as tk
import math
from functools import partial

class Application(tk.Frame):
    #initialize
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_buttons()

    #generate buttons
    def create_buttons(self):
        self.buttons = []

        #'partial' command calls function with that parameter
        self.buttons.append(tk.Button(self, text=str(0), command=partial(self.click_number, 0)))
        self.buttons[0].grid(column=1, row=4, sticky='nesw')
        
        for i in range(1, 10):  #stops at 9
            self.buttons.append(tk.Button(self, text=str(i), command=partial(self.click_number, i)))
            self.buttons[i].grid(column=math.floor((i-1)%3), row=math.ceil(i/3), sticky='nesw')

            #key binding; doesn't work
            #self.buttons[i].bind("<" + str(i) + ">", partial(self.click_number, i))

        self.addButton = tk.Button(self, text=str('+'), command=partial(self.getNextValue, "add"))
        self.addButton.grid(column=4, row=2, sticky='nesw')

        self.subtractButton = tk.Button(self, text=str('-'), command=partial(self.getNextValue, "sub"))
        self.subtractButton.grid(column=5, row=2, sticky='nesw')

        self.multiplyButton = tk.Button(self, text=str('×'), command=partial(self.getNextValue, "mul"))
        self.multiplyButton.grid(column=4, row=3, sticky='nesw')

        self.divideButton = tk.Button(self, text=str('÷'), command=partial(self.getNextValue, "div"))
        self.divideButton.grid(column=5, row=3, sticky='nesw')

        self.clearButton = tk.Button(self, text=str('C'), command=self.clear)
        self.clearButton.grid(column=4, row=1, sticky='nesw')

        self.delButton = tk.Button(self, text=str('⌫'), command=self.backspace)
        self.delButton.grid(column=5, row=1, sticky='nesw')

        self.equalsButton = tk.Button(self, text=str('='), command=self.equals)
        self.equalsButton.grid(column=4, row=4, columnspan=2, sticky='nesw')

        #creates display
        self.display = tk.Text(self, height=2, width=30)
        self.display.configure(font='courier 20')
        self.quote=""
        self.display.insert(tk.END, self.quote)
        self.buttons.append(self.display)
        self.display.grid(column=0,row=0,columnspan=6)

    #add number in
    def click_number(self, i):
        self.toAdd = str(i)
        
        #don't add leading zeros:
        if(i == 0 and len(self.display.get("1.0", "end-1c")) == 0):
            return
        else:
            self.display.insert(tk.END, self.toAdd)

    #clear input
    def clear(self):
        self.display.delete('1.0', tk.END)

    #delete last character entered
    def backspace(self):
        currValue = self.display.get("1.0", "end-1c")
        currValue = currValue[0:-1]
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, currValue)

    #get next value for operation
    def getNextValue(self, oper):
        self.buffer = self.display.get("1.0", "end-1c")
        self.lastFunction = oper
        self.display.delete('1.0', tk.END)

    #execute operation
    def equals(self):
        if(self.lastFunction == "add"):
            self.add(float(self.buffer), float(self.display.get("1.0", "end-1c")))
        elif(self.lastFunction == "sub"):
            self.sub(float(self.buffer), float(self.display.get("1.0", "end-1c")))
        elif(self.lastFunction == "mul"):
            self.mul(float(self.buffer), float(self.display.get("1.0", "end-1c")))
        elif(self.lastFunction == "div"):
            self.div(float(self.buffer), float(self.display.get("1.0", "end-1c")))

    def add(self, one, two):
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, one + two)

    def sub(self, one, two):
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, one - two)

    def mul(self, one, two):
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, one * two)

    def div(self, one, two):
        self.display.delete('1.0', tk.END)
        self.display.insert(tk.END, one / two)
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
