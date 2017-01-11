def mutate_string(string, position, character):
	a = string[:position] + character + string[position+1:]

	# or
	# l = list(string)
	# l[5] = 'k'
	# a = ''.join(l)

	return a


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)