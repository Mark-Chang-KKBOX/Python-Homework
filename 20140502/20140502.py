import sys

def readDataFromFile(fileName):
	with open(fileName) as file:
		lines = file.read().splitlines()
	return [x.replace("\"", "") for x in lines[0].split(',')]

dict = {}
def myFun(str):
	sum = 0
	for i in range(len(str)):
		sum = sum + ord(str[i]) - ord('A') + 1
	dict[str] = sum

if __name__ == '__main__':
	dataList = readDataFromFile(sys.argv[1])
	list(map(myFun, dataList))
	
	i = 1
	sum = 0
	for key in sorted(dict.keys()):
		sum = sum + ( i * dict[key])
		i = i + 1
	
	print(sum)