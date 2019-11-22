# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:37:16 2019

@author: Vishnu Desai
"""

import math
def entropy(P,Hi):
    H=0
    for i in range(a):
        H=H+Hi[i]*P[i]
    return H
    
def state_entropy(p,b):
    H=0
    for i in range(b):
        H=H+(p[i]*math.log2(1/p[i]))
    return H
    
a=int(input('enter number of source alphabets: '))
print('enter ',a,' source alphabets')
S=[]
P=[]
for i in range(a):
    S.append(input(' '))
for i in range(a):
    print('enter probability of ',S[i])
    P.append(float(input(' ')))
p=[]
Hi=[]
for i in range(a):
    print('enter the number of transitions for',S[i])
    b=int(input(' '))
    print('enter ',b,' transition probabilities')
    for j in range(b):
        p.append(float(input(' ')))
    Hi.append(state_entropy(p,b))
for i in range(a):
    print('state entropy of ',S[i],'is ',Hi[i])
H=entropy(P,Hi)
print('source entropy H(S) = ',H)
