# -*- coding: utf-8 -*-

def translate(str):
	t = str
	t = t.replace("*", "乘")
	t = t.replace("=", "等於")	
	t = t.replace("0", "零")
	t = t.replace("1", "一")
	t = t.replace("2", "二")
	t = t.replace("3", "三")
	t = t.replace("4", "四")
	t = t.replace("5", "五")
	t = t.replace("6", "六")
	t = t.replace("7", "七")
	t = t.replace("8", "八")
	t = t.replace("9", "九")
	return t

for x in range(1, 10):
	s = ""
	for y in range(1, 10):
		s = "%s*%s=%s" % (x, y, x * y)
		print(translate(s))
	print("")