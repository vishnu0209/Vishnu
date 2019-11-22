# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:21:58 2019

@author: Vishnu Desai
"""
import math 
def codew(dec,l):
    """conveting a to binary and generating code word"""
    res=''
    for x in range(l):
        whole,dec=str(dec*2).split(".")
        dec=float('.'+dec)
        res+=whole
    return (' '+res)
    
def shannon(q,P,S):
    """shannon Binary encoding"""
    # N=no. of source alphabet, P=their probabilities
    print('P=',P)
    a=[.0]*(q)                     # a is alpha a[i]=a[i-1]+p[i-1]
    s=[]
    l=[0]*q
    p=sorted(P)                   # arranging probabilities in desending order
    p.reverse()
    print('sorted p=',p)
    for i in range(q-1):                   # computing alpha
        a[i+1]=a[i]+p[i]
    print('a=',a)
    for i in range(q):                     # find length of code words
        for j in range(q+1):
            if (2**j) >= (1/p[i]):
                l[i]=j
                break
    print('l=',l)
   # print(' p ',' a ','l','code')
    for i in range(q):                     # generating code words
        s.append(codew(a[i],l[i]))
        print(p[i],a[i],l[i],s[i])
    L=sum([a*b for a,b in zip(p,l)])       # average code length
    H=sum([a*math.log2(1/a) for a in p])   #source entropy
    for i in range(q):                     # assigining the code words
        for j in range(q):
            if P[i]==p[j]:
                S[i]+=s[j]
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
    
# user code 
q=int(input('enter no. of source alphabets: '))
print('enter source alphabets:')
S=['']*q
for i in range(q):
    S[i]=input('')
print('enter probabilities of')
P=[.0]*q
for i in range(q):
    P[i]=float(eval(input('%s: '%S[i])))
shannon(q,P,S)
        
            
            
        
    