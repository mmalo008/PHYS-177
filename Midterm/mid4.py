"""
Midterm problem 4
Michael Malone
"""
import matplotlib.pyplot as plt
import numpy as np

q = -1.
k = 9.*10**9

x=np.linspace(-.5,.5,100)
y=np.linspace(-.5,.5,100)

def r(x,y):
	return np.sqrt(x**2+y**2)
def V(r):
	return (k*q)/r

pot = np.zeros((100,100))
for i in range(100):
	for j in range (100):
		r0=r(x[j],y[i])
		pot[j,i]=V(r0)

plt.imshow(pot)
plt.show()

plt.savefig("problem4.png")
