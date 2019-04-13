#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:12:38 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt


A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])

c=(np.linalg.norm(A-B))
a=(np.linalg.norm(B-C))
b=(np.linalg.norm(C-A))


w=np.array
u=np.array
v=np.array

w = (a*A + b*B)/(a+b) 

print(w)


u = (c*C + b*B)/(c+b) 

print(u)


v = (a*A + c*C)/(a+c) 

print(v)