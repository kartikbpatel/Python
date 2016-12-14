# Function
def read():
	# * is unpacking operator
	# sep is separator
	print(*range(1, int(input()) + 1), sep='')

# Main
read()