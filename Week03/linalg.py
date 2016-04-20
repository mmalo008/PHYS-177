"""
Linear Algebra with voltages
Michael Malone
04/18/16
"""

import numpy as np
import numpy.linalg as lin

#create the matices 
a=np.array([[4,-1,-1,-1],[-1,4,-1,-1],[-1,-1,4,-1],[-1,-1,-1,4]],float)
b=np.array([5,0,5,0],float)
N=len(b)

#Solve using Gaussian elimination
for m in range(N):

	div=a[m,m]
	a[m,:]/=div
	b[m]/=div
	
	for i in range(m+1,N):
		mult = a[i,m]
		a[i,:]-=mult*a[m,:]
		b[i]-=mult*b[m]
x = np.empty(N,float)
for m in range(N-1,-1,-1):
	x[m]=b[m]
	for i in range(m+1,N):
		x[m]-=a[m,i]*x[i]
print x


#solve using lin.solve

print lin.solve(a,b)
