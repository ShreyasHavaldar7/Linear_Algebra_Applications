#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:26:17 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt

def mid_pt(B,C):
    D=(B+C)/2
    return D


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

D=mid_pt(B,C)
E=mid_pt(C,A)
F=mid_pt(B,A)



AD= np.vstack((A,D)).T
BE= np.vstack((B,E)).T
CF= np.vstack((C,F)).T

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

print(line_intersect(AD,CF))
print(line_intersect(AD,BE))
print(line_intersect(BE,CF))
