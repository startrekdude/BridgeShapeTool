"""
In tutorial 2 question 3, we were asked to find the probability that a random bridge hand had shape 64XX
The XX represented a wildcard, such that both 6-4-2-1 and 6-4-3-0 matched.

This is code to help with that.
"""

from string import digits

from .partition import all_bridge_shapes

def parse_wildcard(wildcard):
	"""
	Parses a wildcard specified as a string into a match-tuple
	Each element of the match tuple will be a number that must match
	"""
	
	# force it to all caps
	wildcard = wildcard.upper()
	
	result = []
	acc = "" # accumulator
	
	# go through the string, looking for numbers and Xs
	for c in wildcard:	
		if c not in digits:
			# if c isn't a number, finish off any preceding number first
			if acc:
				result.append(int(acc))
				acc = ""
			if c == "X":
				result.append("X")
		else: # c is a digit
			# careful! 1 could start another number
			if c == "1" and not acc:
				acc = c
			else:
				# this could be finishing another number
				num = acc + c
				result.append(int(num))
				acc = ""
	
	# Phew, that was somewhat complex
	# Make sure result is of length 4
	if len(result) != 4:
		raise ValueError("Wildcard has {} entries; expected 4".format(len(result)))
	
	return tuple(x for x in result if x != "X")

def matches_wildcard(shape, wildcard):
	"Returns whether a shape matches the given parsed wildcard"
	remaining_digits = list(shape)
	for digit in wildcard:
		if digit not in remaining_digits:
			return False
		remaining_digits.remove(digit)
	return True

def all_bridge_shapes_matching_wildcard(wildcard):
	"""
	Generates all bridge shapes that match a given wildcard
	Can throw ValueError if the wildcard is invalid
	"""
	wildcard = parse_wildcard(wildcard)	
	
	for shape in all_bridge_shapes():
		if matches_wildcard(shape, wildcard):
			yield shape