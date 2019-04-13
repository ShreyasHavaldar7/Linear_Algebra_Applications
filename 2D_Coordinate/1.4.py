#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:03:18 2019

@author: shreyas
"""

import numpy as np


    
    
    
def dir_vec(AB):
    
    return np.matmul(AB,dvec)
    

def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

A=np.array([-2,-2])
B=np.array([1,3])

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])
AB= np.vstack((A,B)).T

print(dir_vec(AB))
print(norm_vec(AB))    