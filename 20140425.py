import os
import re

inputFileName = "inputNumber.txt"
outputFileName = "outputNumber.txt"

def xSort(unsorted):
	sorted = [0] * (max(unsorted) + 1)
	for i in range(0, len(unsorted)):
		sorted[unsorted[i]] = unsorted[i]
	return sorted

with open(inputFileName) as file:
	number = file.read().splitlines()
for i in range(len(number)):
	number[i] = int(number[i])
	
sorted = xSort(number)

try:
    os.remove(outputFileName)
except OSError:
    pass

count = 0
for i in range(max(sorted), -1, -1):
	if sorted[i] > 0 and count < 3:
		count = count + 1
		print(sorted[i])
		f = open(outputFileName, "a")
		f.write(str(sorted[i])+'\n')
		f.close()