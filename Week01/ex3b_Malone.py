#Library calls
import numpy as np
import matplotlib.pyplot as plt

#input of data
v_min=float(input('Enter Minimum Velocity: '))
v_max=float(input('Enter Maximum Velocity: '))
h=800.
g=-9.81
##optional data input
"""
h=input('Enter Building Height: ')
"""

#calculation
##create velocity array
v=[]
bin_num=10
bin_size=float((v_max-v_min)/(bin_num-1))
for i in range(bin_num):
	v.append(v_min+bin_size*i)
##midcode test for v
#print v

##create and calculate time array
t=np.ones(bin_num)
for j in range(bin_num):
	t[j]=((-v[j]-np.sqrt(v[j]**2-4.*(.5*g)*(h)))/g)
##midcode test for t
#print t
##Output
#plot
graph=plt.plot(v,t)
plt.xlabel('velocity')
plt.ylabel('time')
plt.show()
#save plot
plt.savefig('fig1.png',format='png')
#ASCII data file

##First attempt
"""
f=open('fall_data.txt','wb')
f.write(data)
f.close
"""

##Numpy method for saving text files
np.savetxt('fall_data', (v,t))
