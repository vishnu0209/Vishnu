# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:15:52 2019

@author: Vishnu Desai
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:27:06 2019

@author: Vishnu Desai
"""
def exten1(q,P,n,S):
    Pn=[[.0]*(q**i) for i in range(1,n+1)]
    Sn=[['']*(q**i) for i in range(1,n+1)]
    Pn[0]=P
    Sn[0]=S
    for i in range(1,n):
        t=0
        for k in range(q**(i)):
            for j in range(q):
                Pn[i][t]=(Pn[0][j])*(Pn[i-1][k])
                Sn[i][t]=(Sn[0][j])+(Sn[i-1][k])
                t=t+1
    print('probabilities of ',n,' extension')
    for i in range(q**n):
        print('%s :'%Sn[n-1][i],'%.4f'%Pn[n-1][i])
    return Sn[n-1],Pn[n-1]

q=int(input('enter no. of source alphabets: '))
print('enter source alphabets:')
S=['']*q
for i in range(q):
    S[i]=input('')
print('enter probabilities of')
P=[.0]*q
for i in range(q):
    P[i]=float(eval(input('%s: '%S[i])))
n=int(input('enter extension'))
exten1(q,P,n,S)




    
        