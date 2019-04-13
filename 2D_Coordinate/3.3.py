#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:29:43 2019

@author: shreyas
"""

import numpy as np
import matplotlib.pyplot as plt

def slope(A,B):
	m = np.zeros((2,1))
	m[0] = (A[1]-B[1])/(A[0]-B[0])#slope of AB
	m[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])#base length
	return m

def coeff(p,A):
	q = np.zeros((2,1))
	q[0] = -1/p[0]#slope of altitude
	q[1] = A[1] - q[0]*A[0]# c of y=mx+c
	return q

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

a = slope(B,C)
b = slope(C,A)
c = slope(A,B)
p = coeff(a,A)
q = coeff(b,B)
r = coeff(c,C)

print (p)
print (q)
print (r)