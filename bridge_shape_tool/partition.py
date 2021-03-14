"""
The list of possible bridge shapes is equal to the integer partitions of 13,
with a length of at most 4.

The integer partitions of any given number are the sequences of positive integers
that sum to that integer. Example:
  5 = 5
  4 + 1 = 5
  3 + 2 = 5
  3 + 1 + 1 = 5
  2 + 2 + 1 = 5
  2 + 1 + 1 + 1 = 5
  1 + 1 + 1 + 1 + 1 = 5

Zeros must be added when formatting bridge shapes; for example, the partition (10, 3)
should be formatted as the bridge shape 10-3-0-0. This is implemented in util.format_shape
"""

def generate_partitions_with_duplicates(n, max_length):
	"""
	Generate all integer partitions of n with length at most max_length
	May include partitions that differ only in order (duplicate partitions)
	"""
	
	# If the maximum length is one, only one partition (the ineteger itself) is possible
	# Of course, that partition is always possible
	yield (n,)
	if max_length == 1:
		return
	
	for x in range(1, n):
		# Otherwise, we try to "bite off" part of the number
		remaining = n - x
		
		# and yield the amount "bitten off" along with all possible partitions of the remainder
		remaining_partitions = generate_partitions(remaining, max_length - 1)
		for y in remaining_partitions:
			yield (x,) + y

def generate_partitions(n, max_length):
	"""
	Generate all integer partitions of n with length at most max_length
	Does __not__ include partitions that differ only in order (duplicate partitions)
	"""
	
	# Maintain a set of the partitions we've seen
	seen = set()
	
	for partition in generate_partitions_with_duplicates(n, max_length):
		# Use the numbers making up the partition in sorted order as a key to test for duplicates
		canonical_partition = tuple(sorted(partition))
		if canonical_partition not in seen:
			seen.add(canonical_partition)
			yield partition

def all_bridge_shapes():
	"Generates all possible bridge shapes"
	for partition in generate_partitions(13, max_length=4):
		# Add zeros as required
		padded = partition + (0,) * (4 - len(partition))
		
		# And bridge shapes traditionally are denoted highest number to lowest number
		shape = tuple(sorted(padded, reverse=True))
		yield shape