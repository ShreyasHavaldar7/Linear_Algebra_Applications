#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:21:11 2019

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

print(line_intersect(AU,BV))
print(line_intersect(CW,BV))
print(line_intersect(AU,CW))
