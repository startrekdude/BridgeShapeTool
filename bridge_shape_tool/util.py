def valid_shape(shape):
	"A valid shape is a 4-tuple adding to 13"
	return len(shape) == 4 and sum(shape) == 13

def format_shape(shape):
	"""
	Formats a shape to be displayed to the user
	Ex: (4, 3, 3, 3) formats as 4-3-3-3
	"""
	assert valid_shape(shape)
	return "-".join(str(x) for x in shape)