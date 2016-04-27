"""
Secant Method for Finding Roots

Michael Malone
04/26/16
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def P(x):
	return x**2-4*x*np.sin(x)+(2*np.sin(x))**2
#plot of P(x)
x=np.linspace(-3,3,100)
y=np.zeros(100)
for i in range(100):
	y[i]=P(x[i])


plt.plot(x,y)
plt.ylabel('P(x)')
plt.show()
plt.savefig('function.png')

#by inspection of graph, roots are at ~0,-2,2
error = 1.e-10
root = [-2,0,2]

for i in range(3):
	x0=root[i]+.01
	#x1=root[i]
	x2=root[i]-P(root[i])*((root[i]-x0)/(P(root[i])-P(x0)))
	while abs(x2-root[i])>error:
		x0=root[i]
		root[i]=x2
		x0=root[i]+1
		x2=root[i]-P(root[i])*((root[i]-x0)/(P(root[i])-P(x0)))
for i in range(3):
	print 'Root number ', i+1, 'is ', root[i]

#compare to scipy
scipyroots= fsolve(P,[-2,0,2])
print 'Scipy finds the roots to be', scipyroots
