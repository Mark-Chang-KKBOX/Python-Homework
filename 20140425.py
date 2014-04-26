
def xSort(unsorted):
	sorted = [0] * (max(unsorted) + 1)
	for i in range(0, len(unsorted)):
		sorted[unsorted[i]] = unsorted[i]
	return sorted
	

number = [2134, 3412, 6421, 8723, 9239, 1234, 2345]
sorted = xSort(number)

count = 0
for i in range(max(sorted), -1, -1):
	if sorted[i] > 0 and count < 3:
		count = count + 1
		print(sorted[i])