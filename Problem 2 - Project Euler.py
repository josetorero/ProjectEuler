# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:31:08 2018

@author: Jose.Torero
"""
#This is a recursive way to calculate de nth fibonacci term

def fib(n):
    if n==1:
        return (1)
    elif n==2:
        return (2)
    else:
        return (fib(n-1)+fib(n-2))

suma = 0
i=1

while fib(i)<4000000:
    if fib(i)%2==0:
        suma+=fib(i)
    i+=1

print (suma)