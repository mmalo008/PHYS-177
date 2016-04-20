"""
Electric Potential Density Plot

Michael Malone
04/14/16
"""
import numpy as np
import matplotlib.pylab as plt

#Input and Assignment
pi=3.14159265
e=8.854187817
def phi(q,r):
	return q/(4*pi*e*(r+1.e-6))
def r1(x,y):
	return np.sqrt((x-(.45))**2+(y)**2)
def r2(x,y):
	return np.sqrt((x-(.55))**2+(y)**2)


#Calc
##Generate points for potential
x=np.linspace(0.,1.,100)
y=np.linspace(-0.5,0.5,100)
z=np.zeros((100,100))
for i in range (100):
	for j in range (100):
		z[i,j]=phi(1,r1(x[i],y[j]))+phi(-1,r2(x[i],y[j]))

plt.imshow(z.T,vmin=-.4,vmax=.4,extent=(-50,50,-50,50))
plt.gray()
plt.show()


##points for Field
w=np.zeros((100,100))
for k in range (100):
	for h in range (100):
		if k<99:
			gradx=z[k+1,h]-z[k,h]
		else:
			gradx=z[k,h]-z[k-1,h]
		if h<99:
			grady=z[k,h+1]-z[k,h]
		else:
			grady=z[k,h]-z[k,h-1]	


		w[k,h]=np.sqrt(gradx**2+grady**2)
plt.imshow(w.T,vmin=-.4,vmax=.4)
plt.gray()
plt.show()
