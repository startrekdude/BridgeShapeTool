"""
Outputs the probability distribution of the shape of a random bridge hand as an HTML table

Why an HTML table? If you open it in Chrome, you can copy paste it into a Google Doc with
formatting intact.

Includes all calculations, in LaTeX denoted by "$$" (like "$$ {4 \choose 1} $$")
Completely coincidentally, there's a Google Docs add-on called Auto-LaTeX Equations that
replaces LaTeX denoted by "$$" with nicely rendered images. (okay, that wasn't a coincidence :)
"""

from .partition import all_bridge_shapes
from .shapecalc import number_of_hands_with_shape, number_of_hands_with_shape_latex, probability_of_hand_with_shape
from .util import format_shape

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