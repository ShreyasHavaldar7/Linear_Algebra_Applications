#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:10:37 2019

@author: shreyas
"""


import numpy as np
import matplotlib.pyplot as plt


A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])

print(np.linalg.norm(A-B))
print(np.linalg.norm(B-C))
print(np.linalg.norm(C-A))