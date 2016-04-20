"""
Integration Types Comparison

Michael Malone
04/06/2016
"""
import numpy as np
from scipy.integrate import simps
import Integral as inte

#Input
def f(x):
	return x**4-2*x+1
N=float(20)
a=0.
b=2.
x=np.arange(a,b,((b-a)/N))
y=f(x)
integral_real= 4.4

#Calculation
##midcode test
"""
print x

print y
"""

##My integrals
mytrap = inte.trap(x,y,a,b)
mysimp = inte.simp(x,y,a,b)
##Intrinsic integrals
theirtrap = np.trapz(y,x=x)
theirsimp = simps(y,x=x,dx=((b-a)/N))
##Trap Error calc
N_error = 10
mytrap_error = np.trapz(y,x=x,dx=((b-a)/N_error))
trap_error = float((1/3)*(theirtrap-theirtrap_error))
##Simp Error cal
theirsimp_error = simps(y,x=x,dx=((b-a)/N_error))
simp_error = float((1/15)*(theirsimp-theirsimp_error))

#Output
print 'My trapezoidal function found the sum to be: ', mytrap
print 'My simpson function found the sum to be: ', mysimp
print 'Their trapezoidal function found the sum to be: ', theirtrap
print 'Their simpson function found the sum to be: ', theirsimp
print 'Their trapezoidal value was found with an error of (+/-) ', trap_error
print 'Their simpson value was found with an error of (+/-)', simp_error
print 'The real value of the integral is, ' integral_real
