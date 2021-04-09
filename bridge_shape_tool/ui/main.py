from tkinter import *

import tkinter.simpledialog as simpledialog 
from .icon_asset import ICON
from .table import shape_gen, expression_gen, hand_gen, probability_gen, extra_gen
from ..plot import plot_shape_distribution_graph
from ..wildcard import all_bridge_shapes_matching_wildcard

#clears anything on the screen
def clear(root):
	list = root.pack_slaves()
	for l in list:
		l.destroy()
	list = root.grid_slaves()
	for l in list:
		l.destroy()

#initializes the program
def init_ui():  
	root = Tk()
	root.title("Bridge Shape Tool")
	root.iconphoto(False, PhotoImage(data=ICON))
	menubar = Menu(root)
	menubar.add_cascade(label="Graph", command=lambda: gen_graph(root))
	menubar.add_cascade(label="Table", command=lambda: gen_table(root))
	menubar.add_cascade(label="Calculator for wildcard variants", command=lambda: gen_extra(root))
	# start out showing something
	gen_graph(root)
	root.config(menu=menubar)
	root.mainloop()

#creates a table for all of the data
def gen_table(root):
	clear(root)
	shape_gen()
	expression_gen()
	hand_gen()
	probability_gen()

#creates a histogram with all of the data included
def gen_graph(root):
	clear(root)
	plot_shape_distribution_graph(root)

#creates a table with all wildcard entries for a given shape in form 64XX, X4XX, 13XXX, etc.
def gen_extra(root):
	clear(root)
	wildcard = simpledialog.askstring("Bridge Shape Wildcard",\
		"Please enter desired shape of size 4 using a combination of numbers and X values. (e.g.64XX or X4XX)")
	try:	
		extra_gen(list(all_bridge_shapes_matching_wildcard(wildcard)))
	except BaseException as e:
		messagebox.showerror(title="ValueError", message=str(e))
