"""
Outputs the probability distribution of the shape of a random bridge hand as an HTML table

Why an HTML table? If you open it in Chrome, you can copy paste it into a Google Doc with
formatting intact.

Includes all calculations, in LaTeX denoted by "$$" (like "$$ {4 \choose 1} $$")
Completely coincidentally, there's a Google Docs add-on called Auto-LaTeX Equations that
replaces LaTeX denoted by "$$" with nicely rendered images. (okay, that wasn't a coincidence :)
"""

from .partition import all_bridge_shapes
from .shapecalc import number_of_hands_with_shape, number_of_hands_with_shape_latex, probability_of_hand_with_shape, number_of_hands_with_shape_written
from .util import format_shape
from tkinter import *

def print_dist_table():
	"Outputs the probability distribution of the shape of a random bridge hand as an HTML table"
	
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	
	print("<style>table, td { border: 1px solid black; border-collapse: collapse; }</style>")
	print("<table>")
	
	for count, shape in data:
		prob = probability_of_hand_with_shape(shape)
		
		print("<tr>")
		print("<td>{}</td>".format(format_shape(shape)))
		print("<td>$$ {} $$</td>".format(number_of_hands_with_shape_latex(shape)))
		print("<td>{:,}</td>".format(count))
		print("<td>{:.12f}</td>".format(prob))
		print("</tr>")
	
	print("</table>")

#creates column with list of all shapes
def shape_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	cols = []
	e.grid(row=0, column=0, sticky=(N, E, W),  padx=5)
	e.insert(END,  "Shape:" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=0, sticky=(N, E, W), padx=5)
		e.insert(END,  format_shape(shape) )    #we add the shape to the column item
		cols.append(e)
		i+=1

	return cols

#creates column with list of all expressions
def expression_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	cols = []
	e.grid(row=0, column=1, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Expression:" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=1, sticky=(N, E, W),  padx=5, ipadx=65)
		e.insert(END, number_of_hands_with_shape_written(shape))
		cols.append(e)
		i+=1

	return cols

#creates column showing the number of each hand
def hand_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	cols = []
	e.grid(row=0, column=2, sticky=(N, E, W),  padx=5)
	e.insert(END,  "# of hands" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=2, sticky=(N, E, W),  padx=5)
		e.insert(END, count)
		cols.append(e)
		i+=1

	return cols

#creates column showing all probabilities
def probability_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	cols = []
	e.grid(row=0, column=3, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Probability" )
	
	for count, shape in data:
		prob = probability_of_hand_with_shape(shape)
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=3, sticky=(N, E, W),  padx=5, ipadx=30)
		e.insert(END, prob)
		cols.append(e)
		i+=1

	return cols

#generates the table associated with wildcard.py program.
def extra_gen(hands):
	i = 1
	cols = []
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=0, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Possible hands for the shape" )
	#creates the
	for shape in hands:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=0, sticky=(N, E, W),  padx=5, ipadx=30)
		e.insert(END, shape)
		cols.append(e)
		i+=1
	i = 1
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=1, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Probability of occuring in a random hand" )
	for shape in hands:
		prob = probability_of_hand_with_shape(shape)
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=1, sticky=(N, E, W),  padx=5, ipadx=60)
		e.insert(END, prob)
		cols.append(e)
		i+=1


	return cols
