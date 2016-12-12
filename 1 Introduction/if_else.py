# Function
def read():
	n = int(input())
	if n%2==1 or (n>=6 and n<=20):
		return "Weird"
	else:
		return "Not Weird"

# Main
my_str = read()
print(my_str)