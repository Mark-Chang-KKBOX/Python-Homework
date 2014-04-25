import sys

number = []
for i in range(1, len(sys.argv)):
	number.append(int(sys.argv[i]))

for i in range(0, len(number)):
	for j in range(i, len(number)):
		if number[i] < number[j]:
			number[i], number[j] = number[j], number[i]
	
for i in range(0, 3):
	print ("%d" % number[i])