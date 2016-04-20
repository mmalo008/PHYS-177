"""
Velocity and Time data to distance Program

Michael Malone
04/06/2016
"""
import numpy as np
import matplotlib.pyplot as plt
import Integral as inte

#Input
data=np.loadtxt("velocities.txt")
time=data[:,0]
vel=data[:,1]
##Mid-code test
"""
for i in range(10):
	print ('Time ', time[i])
for j in range(10):
	print ('Vel ', vel[j])
"""

#Calculation
##Trap distance calulation
trap_sum=inte.trap(time,vel,0.,100.)

##Simp distance calulation
simp_sum=inte.simp(time,vel,0.,100.)

###midcode test
"""
print trap_sum
print simp_sum
"""

#Output
##Save output
Tfile_val=[trap_sum]
np.savetxt('Trap_dist', Tfile_val)
Sfile_val=[simp_sum]
np.savetxt('Simp_dist', Sfile_val)

##Create distance array for final plot
dist=[]
i=0
for i in range(1,102):
	dist.append(inte.simp(time[0:i],vel[0:i],0.,i))


##Plot
"""
fig, axes = plt.subplots(2,1,figsize=(8,4))
axes[0].plot(time,vel)
axes[0].set_title("Velocity curve")
axes[1].plot(time,dist)
axes[1].set_title("Distance curve")

sub1=fig.add_subplot(1,2,1)
sub1.plot(time,vel)
sub2=fig.add_subplot(1,2,2)
sub2.plot(time,dist)
plt.show()
"""

plt.figure(1)
plt.subplot(211)
plt.xlabel('time')
plt.ylabel('velocity')
plt.plot(time,vel)

plt.subplot(212)
plt.xlabel('time')
plt.ylabel('distance')
plt.plot(time,dist)
plt.show()
