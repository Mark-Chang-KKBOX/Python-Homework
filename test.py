import sys
dev

def isValid(inString):
	if len(inString) == 0:
		return False
	
	count = 0
	for x in [y for y in [z for z in inString.split('a>')] if y]:
		if x == "<":
			count = count + 1;
		elif x == "</":				
			count = count - 1;
			if count < 0:
				return False
		else:
			return False
	return count == 0

if __name__ == '__main__':
	print(isValid(sys.argv[1]))