for x in range(1, 10):
	s = ""
	for y in range(1, 10):
		s += "%s*%s=%s\t" % (x, y, x * y)
	print(s)