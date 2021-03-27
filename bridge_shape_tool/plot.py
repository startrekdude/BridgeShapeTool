import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd

from io import BytesIO
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

from .partition import all_bridge_shapes
from .shapecalc import probability_of_hand_with_shape
from .util import format_shape

def calc_plot_data():
	"""
	Calculates the data to plot
	I want the data to be generally mound-shaped, so I make sure the
	highest value is in the middle, and the next-highest are beside it, etc
	"""
	
	# start by getting the probability of every shape
	raw_data = [(probability_of_hand_with_shape(shape), format_shape(shape)) for shape in all_bridge_shapes()]
	
	# sort it high to low
	raw_data.sort(reverse=True)
	
	# now, we order the data to follow a general mound shape
	# first (highest) goes in the middle, then insert all the others to alternating sides in order
	
	mound_shaped_data = [raw_data.pop(0)]
	while raw_data:
		mound_shaped_data.append(raw_data.pop(0))
		if raw_data: mound_shaped_data.insert(0, raw_data.pop(0))
	
	# format the data as all x values, then all y values
	# as expected by matplotlib
	return [val[1] for val in mound_shaped_data], [val[0] for val in mound_shaped_data]

def plot_shape_distribution():
	"""
	Plots the probability distribution of the shape of random bridge hands
	The X-axis is the shape (e.g. "4-3-3-3") and the Y-axis is the probability
	between 0 and 1.
	
	Returns a bytes object containing a PNG image
	"""
	
	# start by getting the data to plot
	x, y = calc_plot_data()
	
	# now, plot the data
	x_pos = list(range(len(x)))
	plt.bar(x_pos, y, width=1.2)
	plt.xticks(x_pos, x, rotation="vertical")
	plt.xlabel("Hand Shape")
	plt.ylabel("Probability")
	
	# save the plotted data
	buf = BytesIO()
	plt.savefig(buf, format="png", bbox_inches='tight')
	buf.seek(0)
	
	return buf.read()

def plot_shape_distribution_graph(root):
	"""
	Plots the probability distribution of the shape of random bridge hands
	The X-axis is the shape (e.g. "4-3-3-3") and the Y-axis is the probability
	between 0 and 1.
	
	Returns a Tkinter canvas with the graph, ready for display
	"""

	# shape data for the x axis and probability to be plotted against the y axis
	x, y = calc_plot_data()
	
	# prepare a DataFrame with the data to be plot
	df = pd.DataFrame(y, x)
	
	# create image frame
	frame = Frame(root)
	frame.pack()

	# create figure
	fig = matplotlib.pyplot.Figure()
	
	# create matplotlib canvas using `fig` and assign to widget `top`
	canvas = FigureCanvasTkAgg(fig, frame)
	canvas.get_tk_widget().pack()

	# create subplot location and names for each axis
	ax1 = fig.add_subplot(211)
	ax1.set_xlabel('Hand Shape')
	ax1.set_ylabel('Probability')

	# draw on this plot
	df.plot(kind='bar', legend=False, ax=ax1, width=1.0)

	return canvas