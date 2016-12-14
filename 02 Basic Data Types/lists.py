# Function
def read():
	n = int(input())
	# define list
	L = []

	for i in range(n):
		# spit input string
		inputstr = input().split()
		# first argument is execution command
		cmd = inputstr[0]
		# second argument and onwards are parameters (optional)
		arg = inputstr[1:]

		if(cmd!="print"):
			# join arg by , and concat with braces ()
			cmd+="("+",".join(arg)+")"
			# concat list with commant and execute using eval
			eval("L."+cmd)
		else:
			print(L)

# Main
read()