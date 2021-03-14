from math import comb

from .util import valid_shape

NUMBER_OF_POSSIBLE_HANDS = comb(52, 13) # "52 choose 13"

def floating_suits(shape):
	"""
	Calculates the number of "floating suits" in a shape
	Take for example the shape 4-3-3-3. It doesn't matter *which* suits
	are assigned to the 3 3's—it's the same thing either way.
	However, the four *does* matter—a hand where the 4 is diamonds is
	different from a hand where the 4 is hearts.
	This is important when calculating the # of possible hands with a shape.
	"""
	assert valid_shape(shape)
	return len(set(shape)) - 1

def number_of_hands_with_shape(shape):
	"Calculates the number of bridge hands with a given shape"
	assert valid_shape(shape)
	
	# The number of bridge hands with a shape is a product of "(n choose k)" numbers
	# Set a variable to the multiplicative identity to start
	product = 1
	
	# Deal first with the floating suits
	floating = floating_suits(shape)
	for x in range(4, 4 - floating, -1):
		# The number of possible choices of suits by this point
		product *= comb(x, 1)
	
	# And now, deal with the # of cards from each suit
	for x in shape:
		product *= comb(13, x)
	
	return product

def probability_of_hand_with_shape(shape):
	"""
	Calculates the probability of a random bridge hand having the given shape
	Here, |S| is number_of_hands_with_shape(shape) and |Ω| is the number of
	possible hands (i.e. 52 choose 13)
	"""
	assert valid_shape(shape)
	return number_of_hands_with_shape(shape) / NUMBER_OF_POSSIBLE_HANDS

def number_of_hands_with_shape_latex(shape):
	"""
	Creates the expression that makes the number of hands with a given shape in latex
	Follows the same algorithm as number_of_hands_with_shape, just outputs a latex
	expression instead of a number
	"""
	assert valid_shape(shape)
	
	# start with an empty string, and add the required latex to it
	result = ""
	
	# Deal first with the floating suits
	floating = floating_suits(shape)
	for x in range(4, 4 - floating, -1):
		# The number of possible choices of suits by this point
		result += "{{{} \\choose 1}}".format(x)
	
	# And now, deal with the # of cards from each suit
	for x in shape:
		result += "{{13 \\choose {}}}".format(x)
	
	return result