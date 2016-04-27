"""
Sixth Order Polynomial Root

Michael Malone
04/26/16
"""
import matplotlib.pyplot as plt
import numpy as np

def P(x):
	return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1

#plot of P(x)
x=np.linspace(0,1,100)
y=P(x)

plt.plot(x,y)
plt.ylabel('P(x)')
plt.show()
plt.savefig('function.png')

#by inspection of graph, roots are at ~.05,.15,.4,.6,.85,.95
##expected root array
#terms are offset so they can enter loop
root = [.0,.2,.35,.65,.8,.95]

#Newton's method for solving non-linear eqns
#derivative of P
def dP(x):
	return 5544.*x**5-13860.*x**4+12600.*x**3-5040.*x**2+840.*x-42
def ddP(x):
	return 27720.*x**4-55440.*x**3+37800.*x**2-10080.*x+840.

error = .0000000001
for i in range(6):
	e=.01
	x = root[i]
	while e>error:
		root[i] -= (P(root[i]))/(dP(root[i]))
		e = abs((-ddP(x)/(2*dP(x)))*(e**2))

for i in range(6):
	print 'Root number ', i+1, 'is ', root[i]

