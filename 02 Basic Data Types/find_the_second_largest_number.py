# Function
def read():
	N = int(input())
	input_list = list(map(int, input().split()))
	
	input_list.sort()
	input_list.reverse()

	for i in range(1, N):
		if input_list[i] != input_list[i-1]:
			print(input_list[i])
			break;

	# big, sbig = -6000, -6000

	# for i in input_list:
	# 	if(i > big)
	# 		big, sbig = i, big
# Main
read()