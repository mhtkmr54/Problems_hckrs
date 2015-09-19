from collections import Counter

str = raw_input(">>")
st = str


a =  len([v for v in Counter(st).values() if v % 2]) <= 1

if a == True:
	print "YES"

else:
	print "NO"

  
