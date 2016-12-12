# Function
def read():
	n = int(input())

	for i in range(n):
	# Below is an alternative way
	# for i in range(0, n):
		print(i*i)
		# Below is an alternative way
		# print(i**2)

# Main
my_str = read()
print(my_str)