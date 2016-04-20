#library calls
import numpy as np
import matplotlib.pyplot as plt

#Data input
#Homework
H=[10.,10.,8.,9.5,3.,9.,0.,6.]
h_weight=.4
#Midterm
M=[10.,10.,10.,10.,8.,5.,10.,7.]
m_weight=.2
#Final
F=[9.,10.,10.,6.,10.,6.,8.,9.]
f_weight=.4

##Optional data input
"""
h_counter=input('Enter Student Homework Grade (q to stop): ')
a=0
while h_counter != q:
	H[a]=(h_counter)
	input('Enter Student Homework Grade (q to stop): ')
	a+=1

m_counter=input('Enter Student Midterm Grade (q to stop): ')
b=0
while m_counter != q:
	M[b]=(m_counter)
	input('Enter Student Midterm Grade (q to stop): ')
	b+=1

f_counter=input('Enter Student Final Grade (q to stop): ')
c=0
while f_counter != q:
	F[c]=(f_counter)
	input('Enter Student Final Grade (q to stop): ')
	c+=1

h_weight=input('Enter Homework Weight: ')
m_weight=input('Enter Midterm Weight: ')
f_weight=input('Enter Final Weight: ')

"""

#Calculation: Assuming the grade weights given in class (HW(40%),MT(20%),F(40%))

#create grade array
G=np.zeros(8)

#rewriting loop and grade output
for i in range(8):
	G[i]=h_weight*H[i]+m_weight*M[i]+f_weight*F[i]
	print G[i]
#Test for failing
##failing counter
num_f=0.
for i in range(8):
	if G[i] < 6.:
		num_f += 1
#Failing output
print 'Number of failing students: ',num_f
for i in range(8):
	if G[i] < 6.:
		print G[i]
#Outstanding test
##outstanding counter
num_o=0.
for i in range(8):
	if G[i] > 9.5:
		num_o += 1

#Outstanding student output
print 'Fraction of outstanding students: ', num_o/8

#Histogram
##create histogram
plt.hist(G,bins=8)
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.show()

##Saving histogram
plt.savefig('hist.png',format='png')

##Saving Grade file
np.savetxt('grades.txt',G, format="10%f")
