# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:53:46 2019

@author: Vishnu Desai
"""

import math
def group(q,p):
    pg=[.0]*2
    diff=[.0]
    for i in range(int(q/2)):
        pg[0]=p[0:i+1]
        pg[1]=p[i+1:q]
        diff.append(abs(sum(pg[1])-sum(pg[0])))
        print('dff=',diff,pg)
        if diff[i]<(diff[i+1]):
            if i>0:
                pg[0]=p[0:i]
                
                pg[1]=p[i:q]
                
                print(1)
                break

    for i in range(2):
        if len(pg[i])!=1:
            pg[i]=group(len(pg[i]),pg[i])
    print(pg)
    return pg
def code(q,g,k,c):
    print('g=',g,k)
    for i in range(2):
        print(k)
        if len(g[i])!=1:
            if i:
                for j in range(k,q):
                    c[j]+=str(i)
            else:
                for j in range(k,k+2):
                    c[j]+=str(i)
            print(c,k)
            c,k=code(q,g[i],k,c)
            
        else:
            c[k]+=str(i)
            k+=1
            print(c,k)
    print(c,k)
    return c,k
        
def shannon_fano(q,P,S):
    print('S=',S)
    print('P=',P)
    l=[0]*q
    p=sorted(P)                 
    p.reverse()
    g=group(q,p)
    k=0
    c=['']*q
    c1,k=code(q,g,k,c)
    for i in range(q):
        l[i]=len(c1[i])
    L=sum([a*b for a,b in zip(p,l)])       # average code length
    H=sum([a*math.log2(1/a) for a in p])   #source entropy
    for i in range(q):                     # assigining the code words
        for j in range(q):
            if P[i]==p[j]:
                S[i]+='-'+c1[j]
                p.remove(p[j])
                p.insert(j,2)
                break
    print('code words=',S)
    print('Average length L=%.4f'%L)
    print('source entropy H(s)=%.4f'%H)
    n=(H/L)*100                            # efficiency n in %
    r=100-n                                # redundency R in %
    print('efficiency n=%.3f'%n,"%")
    print('redundency R=%.3f'%r,"%")
    
    
q=int(input('enter no. of source alphabets: '))
print('enter source alphabets:')
S=['']*q
for i in range(q):
    S[i]=input('')
print('enter probabilities of')
P=[.0]*q
for i in range(q):
    P[i]=float(eval(input('%s: '%S[i])))
shannon_fano(q,P,S)