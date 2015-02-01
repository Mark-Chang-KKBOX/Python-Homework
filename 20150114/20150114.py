# -*- coding: utf-8 -*-

def translate_string(string):
	ts = string

	ts = ts.replace("*", "乘")
	ts = ts.replace("=", "等於")

	ts = ts.replace("0", "零")
	ts = ts.replace("1", "一")
	ts = ts.replace("2", "二")
	ts = ts.replace("3", "三")
	ts = ts.replace("4", "四")
	ts = ts.replace("5", "五")
	ts = ts.replace("6", "六")
	ts = ts.replace("7", "七")
	ts = ts.replace("8", "八")
	ts = ts.replace("9", "九")

	return ts

def translate_number(number):

	if number == 10:
		return "十"

	if number > 10 and number < 20:
		return translate_string("十" + str(number % 10))

	unit = ["", "十"]

	s = str(number)
	a = ""

	while len(s) > 0:
		a += s[0] + unit[len(s) - 1]
		s = s[1:]
	
	ts = a

	if ts.endswith("0"):
		ts = ts[0:len(ts) - 1]
		
	return ts

for x in range(1, 10):
	s = ""
	for y in range(1, 10):
		s = "%s*%s=%s" % (translate_number(x), 
			              translate_number(y), 
			              translate_number(x * y))
		print(translate_string(s))
	print

