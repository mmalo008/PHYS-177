#Library Calls
import numpy as np
import math

#input of data
v=input('Enter Intial Velocity: ')
g=9.81
a=-.5*g
c=800
##optional data input
"""
input('Enter Local Gravity: ')
input('Enter Tower Height: ')
"""
#calculation
##Solve t by quadratic equation
b=np.sqrt(v**2-4*a*c)
t=(-v-b)/(2*a)
print "Time: ", t
