#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:51:59 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt

def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def dir_vec(AB):
    
    return np.matmul(AB,dvec)

def ortho(BC,CA):
    n1=dir_vec(BC)
    n2=dir_vec(CA)
    
    N=np.vstack((n1,n2))
    p=np.zeros(2)
    
    p[0]=np.matmul(n1,A)
    p[1]=np.matmul(n2,B)
    return np.matmul(np.linalg.inv(N),p)

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
AB= np.vstack((A,B)).T
BC= np.vstack((B,C)).T
CA= np.vstack((C,A)).T
H=(ortho(BC,CA))

AH= np.vstack((A,H)).T
BH= np.vstack((B,H)).T
CH= np.vstack((C,H)).T

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

print(line_intersect(AH,BC))
print(line_intersect(BH,CA))
print(line_intersect(CH,AB))




