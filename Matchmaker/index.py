import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbols(x,y):
    global first
    global previousX, previousY
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
            buttons[previousX, previousY]['text'] = ''
            buttons[x,y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True
            
root=Tk()
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [u'\u2702',u'\u2702',u'\u2703',u'\u2703',u'\u2704',u'\u2704',u'\u2705',u'\u2705',u'\u2706',u'\u2706',u'\u2707',u'\u2707',u'\u2708',u'\u2708',u'\u2709',u'\u2709',u'\u2710',u'\u2710',u'\u2711',u'\u2711',u'\u2712',u'\u2712',u'\u2713',u'\u2713']
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbols(x,y), width=3, height=3)
        button.grid(column=x, row=y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

root.mainloop()
