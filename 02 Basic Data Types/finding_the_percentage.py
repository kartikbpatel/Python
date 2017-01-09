n = int(input())
student_marks = {}
dict={}
for _ in range(n):
	name, *line = input().split()

	# Could be split like this
	# line = input().split()
	# name, scores = line[0], line[1:]

	scores = list(map(float, line))
	student_marks[name] = scores
	dict[name] = sum(scores) / float(len(scores))

query_name = input()
print("%.2f" % round(dict[query_name],2))
print("%.2f" % dict[query_name])