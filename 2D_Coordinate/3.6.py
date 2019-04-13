#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:15:40 2019

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

P=(line_intersect(AH,BC))
Q=(line_intersect(BH,CA))
R=(line_intersect(CH,AB))



len =10
lam_1 = np.linspace(0,1,len)

x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CA = np.zeros((2,len))
x_AP = np.zeros((2,len))
x_BQ = np.zeros((2,len))
x_CR = np.zeros((2,len))


for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]=temp1.T
    temp2 = B + lam_1[i]*(C-B)
    x_BC[:,i]=temp2.T
    temp3 = C + lam_1[i]*(A-C)
    x_CA[:,i]=temp3.T
    temp4 = A + lam_1[i]*(P-A)
    x_AP[:,i]=temp4.T
    temp5 = B + lam_1[i]*(Q-B)
    x_BQ[:,i]=temp5.T
    temp6 = C + lam_1[i]*(R-C)
    x_CR[:,i]=temp6.T
  
   
plt.plot(H[0],H[1],'o')
plt.text(H[0] * (1+0.1),H[1] * (1+0.5),'H')

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_BQ[0,:],x_BQ[1,:],label='$BQ$')
plt.plot(x_CR[0,:],x_CR[1,:],label='$CR$')
    
    
plt.plot(A[0],A[1],'o')
plt.text(A[0] * (1+0.1), A[1] * (1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0] * (1-0.2), B[1] * (1),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0] * (1+0.03), C[1] * (1-0.1),'C')
plt.plot(P[0],P[1],'o')
plt.text(P[0] * (1+0.03), P[1] * (1-0.1),'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0] * (1+0.03), Q[1] * (1-0.1),'Q')
plt.plot(R[0],R[1],'o')
plt.text(R[0] * (1+0.3), R[1] * (1+0.1),'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
