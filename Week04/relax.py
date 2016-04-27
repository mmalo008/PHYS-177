"""
2-D Relaxation Method 

Michael Malone
"""
import numpy as np

a=1.
b=2.
x=1.
y=1.
numtries = 20
"""
def func1(x,y):
	return y*(a+x**2)
def func2(x):
	return b/(a+x**2)
"""
def func1(x):
	return x/(x**2+a)
def func2(y):
	return np.sqrt((b-a*y)/y)
print x,y

for i in range(20):
	x = func2(y);
	y = func1(x);
	print x,y
