import os, sys

def readNumberFromFile(fileName):
	with open(fileName) as file:
		number = file.read().splitlines()
	for i in range(len(number)):
		number[i] = int(number[i])
	return number

def writeThreeBiggestNumberToFile(fileName, sorted):
	try:
		os.remove(fileName)
	except OSError:
		pass

	count = 0
	for i in range(max(sorted), -1, -1):
		if sorted[i] > 0 and count < 3:
			count = count + 1
			print(sorted[i])
			f = open(fileName, "a")
			f.write(str(sorted[i])+'\n')
			f.close()
	
def xSort(unsorted):
	sorted = [0] * (max(unsorted) + 1)
	for i in range(0, len(unsorted)):
		sorted[unsorted[i]] = unsorted[i]
	return sorted

if __name__ == '__main__':
	number = readNumberFromFile(sys.argv[1])
	sorted = xSort(number)
	writeThreeBiggestNumberToFile("outputNumber.txt", sorted)
