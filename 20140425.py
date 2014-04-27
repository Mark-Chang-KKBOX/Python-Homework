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
	
threeBiggestNumber = []
def getMaxNumber(numbers):
	maxValue = 0 if len(numbers) == 0 else numbers[0]
	
	for i in range(1, len(numbers)):
		if numbers[i] > maxValue:
			maxValue = numbers[i]
	threeBiggestNumber.append(maxValue)
	
	numbers.remove(maxValue) if len(numbers) > 0 else numbers
	
if __name__ == '__main__':
	numbers = readNumberFromFile(sys.argv[1])
	getMaxNumber(numbers)
	getMaxNumber(numbers)
	getMaxNumber(numbers)
	writeNumberToFile("outputNumber.dat", threeBiggestNumber)
	