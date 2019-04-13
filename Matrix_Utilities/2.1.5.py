#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 01:46:07 2019

@author: shreyas
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

A=np.matrix('1 0; 1 1; 1 2')

b=np.matrix('6; 0; 0')

U, s, V=LA.svd(A)
mn=A.shape

S= np.zeros(mn)

Sinv = S.T
S[:2,:2] = np.diag(s)

print(U.dot(S).dot(V))

sinv=1./s

Sinv[:2,:2] = np.diag(sinv)
print(Sinv)

Aplus = V.T.dot(Sinv).dot(U.T)
x_ls = Aplus.dot(b)

print(x_ls)

