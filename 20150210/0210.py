def check_rule(number):
	return number % 7 == 0 and not(number % 5 == 0)

def print_list(number_list):
	s = ""
	for number in number_list:
		s += str(number) + ", "
	print(s[:len(s) - 2])

print_list(filter(check_rule, range(2000, 3200 + 1)))
