# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:42:55 2024

@author: peter
"""

def ack(n,m):
    print('Aufruf ack(',n,',',m,')')
    if n==0:
        return m+1
    else:
        if m==0:
            return ack(n-1,1)
        else:
            return ack(n-1,ack(n,m-1))
        
        
print('Berechnung der Ackermann Funktion ack(n,m)')
n=int(input('n:'))
m=int(input('m:'))

a=ack(n,m)

print('Ergebnis:',a)