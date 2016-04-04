import numpy as np
#f=np.ones(2)

f=[1,1]
n=len(f)
while f[n-1]<1000:
	print (f[n-1],n)
	n=len(f)
	f.append(f[n-2]+f[n-1])
print f
