# -*- coding: utf-8 -*-

def translate_string(string):
	ts = str(string)

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
	'''
	Special case

	0  = 零
	10 = 十
	18 = 十8 = 十八
	'''
	if number == 0:
		return translate_string(number)

	if number == 10:
		return "十"

	if number > 10 and number < 20:
		return translate_string("十" + str(number % 10))

	'''
	100  = 1百*
	2000 = 2千*
	105  = 1百*5
	2005 = 2千*5
	'''
	unit = ["", "十", "百", "千", "萬"]

	s = str(number)
	ts = ""

	while len(s) > 0:
		if s[0] == "0" and len(s) >= 1:
			if not ts.endswith("*"):
				ts += "*"
		else:
			ts += s[0] + unit[len(s) - 1]
		
		s = s[1:]
	
	''' 
	1百* = 一百
	2千* = 二千
	'''
	while ts.endswith("*"):
		ts = ts[:len(ts) - 1]

	'''
	1百*5 = 1百零5
	2千*5 = 2千零5
	'''
	ts = ts.replace("*", "零")

	return translate_string(ts)


for x in range(1, 10):
	s = ""
	for y in range(1, 10):
		s = "%s*%s=%s" % (translate_number(x), 
			              translate_number(y), 
			              translate_number(x * y))
		print(translate_string(s))
	print


# test case of translate_number()

# print(translate_number(0))
# print(translate_number(5))
# print(translate_number(10))
# print(translate_number(15))
# print(translate_number(50))
# print(translate_number(65))
# print(translate_number(100))
# print(translate_number(105))
# print(translate_number(150))
# print(translate_number(157))
# print(translate_number(2000))
# print(translate_number(2005))
# print(translate_number(2050))
# print(translate_number(2600))
# print(translate_number(2057))
# print(translate_number(2160))
# print(translate_number(3157))
# print(translate_number(10000))
# print(translate_number(10200))
# print(translate_number(10030))
# print(translate_number(10004))
# print(translate_number(10204))
# print(translate_number(10240))
# print(translate_number(10041))
# print(translate_number(12057))
# print(translate_number(12000))
# print(translate_number(12005))
# print(translate_number(12050))