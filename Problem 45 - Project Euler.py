# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

T=[]
P=[]
H=[]

count=0
n=1

while count!=3:
    T.append(int(n*(n+1)/2))
    P.append(int(n*(3*n-1)/2))
    H.append(n*(2*n-1))
    if (T[n-1] in P) and (T[n-1] in H):
        count+=1
    n+=1

print (T[-1])
    