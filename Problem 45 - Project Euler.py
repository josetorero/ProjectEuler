# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


T=[] #List where Trinagular numbers will be stored
P=[] #List where pentagonal numbers will be stored
H=[] #list where hexagonals numbers will be stored

count=0 #This variable will increase when one number appears in all the three lists mentioned before
n=1 #This variable will help us to add elements in the list

while count!=3: #We know 2 numbers that are pentagonal, triangular and hexagonal at the same time: 1 and 40755. The question requires us to find the third number that is pentagonal, trinagular and hexagonal. Count will increase when the former criteria is meet.  
    T.append(int(n*(n+1)/2))
    P.append(int(n*(3*n-1)/2))
    H.append(n*(2*n-1))
    if (T[n-1] in P) and (T[n-1] in H): #We check if the new trinagular number is hexagonal and pentagonal. We use elements in the T list because the elements in H and P lists grow faster.
        count+=1
    n+=1

print (T[-1])
