# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:31:08 2018

@author: Jose.Torero
"""

s=0
for i in range (3,1000):
    if i%3==0 or i%5==0:
        s+=i
        
print (s)        