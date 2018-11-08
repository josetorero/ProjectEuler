# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:42:04 2018

@author: Jose
"""

#We compare continiuolsy three series the hexagonal series, the pentagonal series, and the trinagular series
#The Hexagonal series grows faster thant the other two
#The i-ih term in the hexagonal series will be always higher than the i-th term in the other two series
#The i-ih term in the pentagonal series will be always higher than the i-th term in triangle series
#So we generate terms in both series and look if the last term of both are included in the largest series

hexg=[0] #hexagonal series
pen=[0] #pentagonal series
tri=[0] #trinagular series
final=[]
i=1

while len(final)<3: #question requires the third number that meet all the criterias, first one is 1, and the second one is 40755 
    hexg.append(int(i*(2*i-1)))
    pen.append(int(i*(3*i-1)/2))
    tri.append(int(i*(i+1)/2))
    if pen[-1] in hexg and tri[-1] in hexg:
        final.append(pen[-1])
        
    i+=1

print (final[-1])