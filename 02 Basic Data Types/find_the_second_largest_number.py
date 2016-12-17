# Function
def read():
	N = int(input())
	input_list = list(map(int, input().split()))
	
	# Method-1
	input_list.sort()
	input_list.reverse()

	for i in range(1, N):
		if input_list[i] != input_list[i-1]:
			print(input_list[i])
			break;

	# Method-2
	# big, sbig = -6000, -6000
	# for i in input_list:
	# 	if(i > big):
	# 		big, sbig = i, big
	# 	elif(i < big and i > sbig):
	# 		sbig = i
	# print(sbig)

	# Method-3
	# z = max(input_list)
	# for _ in input_list:
	# 	if max(input_list)==z:
	# 		input_list.remove(max(input_list))
	# print(max(input_list))

	# Method-4
	# z = max(input_list)
	# while max(input_list)==z:
	# 		input_list.remove(max(input_list))
	# print(max(input_list))

# Main
read()