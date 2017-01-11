def swap_case(s):
	a = ''.join([a.lower() if a.isupper() else a.upper() for a in s])
	return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)