def split_and_join(s):
	# a = '-'.join(s.split(" "))
	# Or
	a = s.replace(" ","-")
	return a

if __name__ == '__main__':
    s = input()
    result = split_and_join(s)
    print(result)