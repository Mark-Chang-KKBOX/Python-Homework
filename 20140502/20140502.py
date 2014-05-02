import sys
from functools import reduce 

def readDataFromFile(fileName):
	with open(fileName) as file:
		lines = file.read().splitlines()
	return [x.replace("\"", "") for x in lines[0].split(',')]

dict = {}
def stringToNumber(str):
	sum = 0
	for i in range(len(str)):
		sum = sum + ord(str[i]) - ord('A') + 1
	dict[str] = sum

if __name__ == '__main__':
	list(map(stringToNumber, readDataFromFile(sys.argv[1])))
	print (reduce(lambda x, y : x + y, [dict[x] * (index + 1) for index, x in enumerate(sorted(dict.keys()))]))