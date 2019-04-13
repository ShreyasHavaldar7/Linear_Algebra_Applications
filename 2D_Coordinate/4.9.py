#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:27:15 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt


def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def line_intersect(AD,CF):
    n1=norm_vec(AD)
    n2=norm_vec(CF)
    
    N=np.vstack((n1,n2))
    p=np.zeros(2)
    
    p[0]=np.matmul(n1,AD[:,0])
    p[1]=np.matmul(n2,CF[:,0])
    return np.matmul(np.linalg.inv(N),p)

def coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p


def line_dist(I,p):
	return np.abs((I[0]*p[0]-I[1]+p[1])/(np.sqrt(p[0]**2+1)))



A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])

c=(np.linalg.norm(A-B))
a=(np.linalg.norm(B-C))
b=(np.linalg.norm(C-A))


W=np.array
U=np.array
V=np.array

W = (a*A + b*B)/(a+b) 

U = (c*C + b*B)/(c+b) 

V = (a*A + c*C)/(a+c) 


AU= np.vstack((A,U)).T
BV= np.vstack((B,V)).T
CW= np.vstack((C,W)).T

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

I=(line_intersect(AU,BV))


AB = coeff(A.T,B.T)
BC = coeff(B.T,C.T)
CA = coeff(C.T,A.T)


print(line_dist(I.T,AB))
print(line_dist(I.T,BC))
print(line_dist(I.T,CA))
