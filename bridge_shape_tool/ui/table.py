from tkinter import *

from ..partition import all_bridge_shapes
from ..shapecalc import number_of_hands_with_shape, number_of_hands_with_shape_written, probability_of_hand_with_shape
from ..util import format_shape

#creates column with list of all shapes
def shape_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=0, sticky=(N, E, W),  padx=5)
	e.insert(END,  "Shape:" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=0, sticky=(N, E, W), padx=5)
		e.insert(END,  format_shape(shape) )    #we add the shape to the column item
		i+=1

#creates column with list of all expressions
def expression_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=1, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Expression:" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=1, sticky=(N, E, W),  padx=5, ipadx=65)
		e.insert(END, number_of_hands_with_shape_written(shape))
		i+=1

#creates column showing the number of each hand
def hand_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=2, sticky=(N, E, W),  padx=5)
	e.insert(END,  "# of hands" )
	
	for count, shape in data:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=2, sticky=(N, E, W),  padx=5)
		e.insert(END, "{:,}".format(count))
		i+=1

#creates column showing all probabilities
def probability_gen():
	i = 1
	# We get all our data together first, mostly so we can order it from most to least likely
	data = [(number_of_hands_with_shape(shape), shape) for shape in all_bridge_shapes()]
	# Because it's a tuple and count is the first field, it will sort by count
	data.sort(reverse=True)
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=3, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Probability" )
	
	for count, shape in data:
		prob = probability_of_hand_with_shape(shape)
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=3, sticky=(N, E, W),  padx=5, ipadx=30)
		e.insert(END, prob)
		i+=1

#generates the table associated with wildcard.py program.
def extra_gen(hands):
	# first we do all possible shapes for the wildcard
	i = 1
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=0, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Possible shapes for the wildcard" )
	#creates the
	for shape in hands + ["Sum"]:
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=0, sticky=(N, E, W),  padx=5, ipadx=30)
		e.insert(END, shape)
		i+=1
	
	# then we do the number of hands in each shame
	i = 1
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=1, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "# of hands for this shape" )
	
	# track the sum of every probability
	sum = 0
	for shape in hands + [-1]: # -1: sentinel value to display sum
		if shape != -1:
			count = number_of_hands_with_shape(shape)
			sum += count
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=1, sticky=(N, E, W),  padx=5, ipadx=60)
		
		if shape != -1:
			e.insert(END, "{:,}".format(count))
		else:
			e.insert(END, "{:,}".format(sum))
		i+=1
	
	# then the probability of each hand
	i = 1
	e = Entry(relief=GROOVE)
	e.grid(row=0, column=2, sticky=(N, E, W),  padx=5, ipadx=30)
	e.insert(END,  "Probability of occuring in a random hand" )
	
	# track the sum of every probability
	sum = 0
	for shape in hands + [-1]: # -1: sentinel value to display sum
		if shape != -1:
			prob = probability_of_hand_with_shape(shape)
			sum += prob
		e = Entry(relief=GROOVE)
		e.grid(row=i, column=2, sticky=(N, E, W),  padx=5, ipadx=60)
		
		if shape != -1:
			e.insert(END, prob)
		else:
			e.insert(END, sum)
		i+=1