#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:09:39 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt

def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def dir_vec(AB):
    
    return np.matmul(AB,dvec)

def line_intersect(BC,CA):
    n1=dir_vec(BC)
    n2=dir_vec(CA)
    
    N=np.vstack((n1,n2))
    p=np.zeros(2)
    
    p[0]=np.matmul(n1,A)
    p[1]=np.matmul(n2,B)
    return np.matmul(np.linalg.inv(N),p)



A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])

AB= np.vstack((A,B)).T
BC= np.vstack((B,C)).T
CA= np.vstack((C,A)).T


dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

print(line_intersect(BC,CA))