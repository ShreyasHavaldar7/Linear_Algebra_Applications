#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:37:16 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt

def mid_pt(B,C):
    D=(B+C)/2
    return D

  
    
def dir_vec(AB):
    
    return np.matmul(AB,dvec)
    





  


A=np.matrix('-2;-2')
B=np.matrix('1;3')
C=np.matrix('4;-1')

D=mid_pt(B,C)
E=mid_pt(C,A)
F=mid_pt(B,A)

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

AD= np.vstack((A.T,D.T)).T
BE= np.vstack((B.T,E.T)).T
CF= np.vstack((C.T,F.T)).T

print(dir_vec(AD))
print(dir_vec(BE))
print(dir_vec(CF))





