"""
Integral Library

Michael Malone
04/07/2016
"""
import numpy as np

def trap(x,y,a,b):
	N = len(y)
	h=(b-a)/float(N)
	s=0.5*y[0]+0.5*y[-1]
	for k in range (1,int(N),1):
		s+=y[k]
	return s*h


def simp(x,y,a,b):
	N=len(y)
	h=(b-a)/N
	s=y[0]+y[-1]
	for O in range (1,int(N),2):
		s+=4*y[O]
	for E in range (2,int(N),2):
		s+=2*y[E]
	return s*(h/3)
	
