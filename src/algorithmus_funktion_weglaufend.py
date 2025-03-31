# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:24:22 2024

@author: peter
"""

N = 6
f = [0 for i in range(0, N + 1)]

for i in range(1, N + 1):
    f[i] = 2 ** f[i - 1]
    print("f[", i, "] ist ", f[i])
