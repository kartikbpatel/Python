import re

def count_substring(string, sub_string):
	str_len = len(string)
	sub_str_len = len(sub_string)
	cnt = 0
	for i in range(0, str_len-sub_str_len+1):
		if string[i:i+sub_str_len] == sub_string:
			cnt += 1
	return cnt
	
	# or
	# match = re.findall('(?='+sub_string+')',string)
	# return len(match)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)