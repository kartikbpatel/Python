# Function
def read():
	n = int(input())

	 # map(aFunction, aSequence) 
	integer_list = map(int, input().split())

	# Tuples are sequences, just like lists but can't change and use parentheses ( & )
	t = tuple(integer_list)
	print(hash(t))

# Main
read()