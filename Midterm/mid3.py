"""
Midterm problem 3
Michael Malone
"""
import matplotlib.pyplot as plt
import numpy as np

def y(t):
	return (-3*t**5)-(24*t**4)+(3*t)+10

t=np.linspace(0,10**9,20)
height = y(t)
plt.plot(t,height)
plt.show()

#y=0 almost instantly. I hade to alter the 1Gyr to 1 yr to find that it is around t = .8yr

def yprime(t):
	return (-15*t**4)-(96*t**3)+3
def ypp(t):
	return (-60*t**3)-(288*t**2)
#first guess
t0=.6
error = 10**-10
steps = 0
t1 = t0-(y(t0)/yprime(t0))
while abs(t1-t0)>error:
	t0=t1
	t1=t1-(y(t1)/yprime(t1))
	steps += 1

print "Comet passes equator at ,", t1, " years, and it took, ", steps, " steps to find that root."

