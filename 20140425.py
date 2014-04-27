import os, sys

def readNumberFromFile(fileName):
	with open(fileName) as file:
		number = file.read().splitlines()
	for i in range(len(number)):
		number[i] = int(number[i])
	return number


def writeNumberToFile(fileName, number):
	try:
		os.remove(fileName)
	except OSError:
		pass

	for i in range(len(number)):
		print(number[i])
		f = open(fileName, "a")
		f.write(str(number[i])+'\n')
		f.close()
	
def xSort(unsorted):
	sorted = [0] * (max(unsorted) + 1)
	for i in range(0, len(unsorted)):
		sorted[unsorted[i]] = unsorted[i]
	return sorted


threeBiggestNumber = []
def getMaxNumber(number):
	maxValue = number[0]
	for i in range(1, len(number)):
		if number[i] > maxValue:
			maxValue = number[i]
	
	threeBiggestNumber.append(maxValue)
	number.remove(maxValue)
	
if __name__ == '__main__':
	number = readNumberFromFile(sys.argv[1])
	getMaxNumber(number)
	getMaxNumber(number)
	getMaxNumber(number)
	writeNumberToFile("outputNumber.dat", threeBiggestNumber)
	