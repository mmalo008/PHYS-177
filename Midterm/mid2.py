"""
Midterm prob2

Michael Malone
"""
x = 1
y = 1
z = 0
for i in range(10):
	z = x+y
	x = y
	y = z
print "The twelfth Fibonacci term is: ", y

x = 1.
y = 1.
z = 0.
for i in range(98):
	z = x+y
	x = y
	y = z
print "The ratio of the one hundtreth and the ninty ninth term is: ", y/x	
