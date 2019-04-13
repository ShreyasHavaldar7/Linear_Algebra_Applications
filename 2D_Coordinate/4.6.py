#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:24:30 2019

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





len =10
lam_1 = np.linspace(0,1,len)

x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CA = np.zeros((2,len))
x_AU = np.zeros((2,len))
x_BV = np.zeros((2,len))
x_CW = np.zeros((2,len))


for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]=temp1.T
    temp2 = B + lam_1[i]*(C-B)
    x_BC[:,i]=temp2.T
    temp3 = C + lam_1[i]*(A-C)
    x_CA[:,i]=temp3.T
    temp4 = A + lam_1[i]*(U-A)
    x_AU[:,i]=temp4.T
    temp5 = B + lam_1[i]*(V-B)
    x_BV[:,i]=temp5.T
    temp6 = C + lam_1[i]*(W-C)
    x_CW[:,i]=temp6.T
  
I=(line_intersect(AU,BV))
plt.plot(I[0],I[1],'o')
plt.text(I[0] * (1+0.1), I[1] * (1+0.5),'I')

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AU[0,:],x_AU[1,:],label='$AU$')
plt.plot(x_BV[0,:],x_BV[1,:],label='$BV$')
plt.plot(x_CW[0,:],x_CW[1,:],label='$CW$')
    
    
plt.plot(A[0],A[1],'o')
plt.text(A[0] * (1+0.1), A[1] * (1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0] * (1-0.2), B[1] * (1),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0] * (1+0.03), C[1] * (1-0.1),'C')
plt.plot(U[0],U[1],'o')
plt.text(U[0] * (1+0.03), U[1] * (1-0.1),'U')
plt.plot(V[0],V[1],'o')
plt.text(V[0] * (1+0.03), V[1] * (1-0.1),'V')
plt.plot(W[0],W[1],'o')
plt.text(W[0] * (1-0.3), W[1] * (1-0.1),'W')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
