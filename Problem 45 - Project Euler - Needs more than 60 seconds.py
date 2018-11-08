# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:35:31 2018

@author: Jose
"""
#The Hexagonal series grows faster, so in order to make less computations we will verfy Hexagonal numbers with 
#the other series

#This function checks if the number is Pentagonal
def isPen(n):
    s=[1]
    i=2
    while s[-1]<n:
        s.append(int(i*(3*i-1)/2))
        i+=1
    if n in s:
        return True
    else:
        return False
    
#This function checks if the number is triangular
def isTri(n):
    s=[1]
    i=2
    while s[-1]<n:
        s.append(int(i*(i-1)/2))
        i+=1
    if n in s:
        return True
    else:
        return False

f=[]
i=1
c=1

while len(f)<3: #Answer requested is the third number that meet all criterias, first one is 1, and the second one is 40755
    if isPen(c):
        if isTri(c):
            f.append(c)
    i+=1
    c=i*(2*i-1) #This is the criteria for Hexagonal numers

print(f[2])

#Program requires almost 3 minutes to find the answer, so I'll be thinking in a faster solution