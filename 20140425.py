
unsort = [2134, 3412, 6421, 8723, 9239,1234, 2345]

temp = unsort[0]
unsort[0] = unsort[1]
unsort[1] = temp

for aa in unsort:
	print("%d, " % aa)