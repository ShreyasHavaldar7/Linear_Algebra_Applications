#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:27:18 2019

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


len =10
lam_1 = np.linspace(0,1,len)

x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CA = np.zeros((2,len))
x_AD = np.zeros((2,len))
x_BE = np.zeros((2,len))
x_CF = np.zeros((2,len))


for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]=temp1.T
    temp2 = B + lam_1[i]*(C-B)
    x_BC[:,i]=temp2.T
    temp3 = C + lam_1[i]*(A-C)
    x_CA[:,i]=temp3.T
    temp4 = A + lam_1[i]*(D-A)
    x_AD[:,i]=temp4.T
    temp5 = B + lam_1[i]*(E-B)
    x_BE[:,i]=temp5.T
    temp6 = C + lam_1[i]*(F-C)
    x_CF[:,i]=temp6.T
  
G=line_intersect(AD,CF)    
plt.plot(G[0],G[1],'o')
plt.text(G[0] * (1+0.1), G[1] * (1+0.5),'G')

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')
    
    
plt.plot(A[0],A[1],'o')
plt.text(A[0] * (1+0.1), A[1] * (1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0] * (1-0.2), B[1] * (1),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0] * (1+0.03), C[1] * (1-0.1),'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0] * (1+0.03), D[1] * (1-0.1),'D')
plt.plot(E[0],E[1],'o')
plt.text(E[0] * (1+0.03), E[1] * (1-0.1),'E')
plt.plot(F[0],F[1],'o')
plt.text(F[0] * (1-0.3), F[1] * (1-0.1),'F')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
