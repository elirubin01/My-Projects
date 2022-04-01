from tkinter import *
from tkinter import ttk
import random

global target
target = random.randrange(1, 100)
global tries
tries = 0


def guess(*args):
	try:
		global tries
		global target
		tries += 1
		x = int(num.get())
		if x == target:
			hint.set("You win! Score: " + str(tries))
		if x < target:
			hint.set("Too low.")
		if x > target:
			hint.set("Too high.")
		numBox.delete(0, 'end')
	except ValueError:
		hint.set("Your guess must be an integer.")


game = Tk()
game.title("Guessing Game")

mainframe = ttk.Frame(game, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

game.columnconfigure(0, weight = 1)
game.rowconfigure(0, weight = 1)

num = StringVar()
numBox = ttk.Entry(mainframe, width = 5, textvariable = num)
numBox.grid(column = 2, row = 1, sticky = (W, E))

hint = StringVar()
ttk.Label(mainframe, textvariable = hint).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = "Guess", command = guess).grid(column = 3, row = 3, sticky = (W, E))

for child in mainframe.winfo_children():
	child.grid_configure(padx = 5, pady = 5)
numBox.focus()
game.bind("<Return>", guess)

game.mainloop()