from sys import argv as args

from .disttable import print_dist_table
from .partition import all_bridge_shapes
from .plot import plot_shape_distribution
from .shapecalc import number_of_hands_with_shape
from .ui.main import init_ui
from .util import format_shape
from .wildcard import all_bridge_shapes_matching_wildcard

def main():
	"""
	Entry point for BridgeShapeTool
	Determines what to do based on the command line, and does it
	"""
	
	if len(args) < 2:
		init_ui()
	else:
		verb = args[1]
		if verb == "test_math":
			test_math()
		elif verb == "print_dist_table":
			print_dist_table()
		elif verb == "save_plot":
			save_plot()
		elif verb == "test_wildcard":
			test_wildcard()

def save_plot():
	"Saves the distribution plot generated by plot_shape_distribution to a file"
	with open("plot.png", "wb") as f:
		f.write(plot_shape_distribution())

def test_wildcard():
	"""
	Tests the wildcard functionality by asking the user to enter a wildcard
	and printing all matches.
	NOTE: crashes with ValueError on invalid wildcard, remember to catch this
	for anything user facing
	"""
	wildcard = input("Wildcard? ")
	print(list(all_bridge_shapes_matching_wildcard(wildcard)))

def test_math():
	"""
	Tests the math implemented in BridgeShapeTool by calculating the # of hands
	for all possible bridge shapes and comparing it to known correct answers
	"""
	our_answers = {shape: number_of_hands_with_shape(shape) for shape in all_bridge_shapes()}
	
	# taken from https://ganeshabridge.com/dist.html
	known_good = {
		(4, 4, 3, 2): 136_852_887_600,
		(5, 3, 3, 2): 98_534_079_072,
		(5, 4, 3, 1): 82_111_732_560,
		(5, 4, 2, 2): 67_182_326_640,
		(4, 3, 3, 3): 66_905_856_160,
		(6, 3, 2, 2): 35_830_574_208,
		(6, 4, 2, 1): 29_858_811_840,
		(6, 3, 3, 1): 21_896_462_016,
		(5, 5, 2, 1): 20_154_697_992,
		(4, 4, 4, 1): 19_007_345_500,
		(7, 3, 2, 1): 11_943_524_736,
		(6, 4, 3, 0): 8_421_716_160,
		(5, 4, 4, 0): 7_895_358_900,
		(5, 5, 3, 0): 5_684_658_408,
		(6, 5, 1, 1): 4_478_821_776,
		(6, 5, 2, 0): 4_134_297_024,
		(7, 2, 2, 2): 3_257_324_928,
		(7, 4, 1, 1): 2_488_234_320,
		(7, 4, 2, 0): 2_296_831_680,		
		(7, 3, 3, 0): 1_684_343_232,
		(8, 2, 2, 1): 1_221_496_848,
		(8, 3, 1, 1): 746_470_296,
		(8, 3, 2, 0): 689_049_504,
		(7, 5, 1, 0): 689_049_504,
		(6, 6, 1, 0): 459_366_336,
		(8, 4, 1, 0): 287_103_960,
		(9, 2, 1, 1): 113_101_560,
		(9, 3, 1, 0): 63_800_880,
		(9, 2, 2, 0): 52_200_720,
		(7, 6, 0, 0): 35_335_872,
		(8, 5, 0, 0): 19_876_428,
		(10, 2, 1, 0): 6_960_096,
		(9, 4, 0, 0): 6_134_700,
		(10, 1, 1, 1): 2_513_368,
		(10, 3, 0, 0): 981_552,
		(11, 1, 1, 0): 158_184,
		(11, 2, 0, 0): 73_008,
		(12, 1, 0, 0): 2_028,
		(13, 0, 0, 0): 4
	}
	
	# compare our_answers to known_good and print the results
	for shape in known_good:
		right_count = known_good[shape]
		our_count = our_answers[shape] if shape in our_answers else "N/A"
		result = "PASS" if our_count == right_count else "FAIL"
		
		print(format_shape(shape))
		print("-- Correct: {}".format(right_count))
		print("-- Ours: {}".format(our_count))
		print("-- Result: {}".format(result))
		print()