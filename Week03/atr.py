"""
Adaptive Trapezoidal Rule

Michael Malone
04/14/2016
"""
import numpy as np

def f(x):
	return (np.sin(np.sqrt(100.*x)))**2
#Input
error_final=.000001
##error counter set to one so loop can be entered
a=0.
b=1.
e=1.
N=1
I_i=0.
I_j=0.


#Calculation
x=np.linspace(a,b,(N+1))
y=f(x)	
I_i=np.trapz(y)

##Loop
while e>error_final:
	N*=2
	x=np.linspace(a,b,(N+1))
	y=f(x)	
	I_j=I_i
	I_i=.5*I_j
	for i in range (1,N,2):
		I_i+=((b-a)/N)*y[i]

	e=abs(float((1./3.)*(I_i-I_j)))
	
	print 'Number of bins: ',N,'Integral: ',I_i,'Error: ',e

print 'End program'

