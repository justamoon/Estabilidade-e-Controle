# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:45:21 2021

@author: Renan
"""

import numpy as np
import matplotlib.pyplot as plt

x = 779.43 / 1000
S = 0.938
b = 2.04
c_medium = 0.462
AR = 2.5
teta = np.pi/9
l_ht = 0.67874
# l_ht = (x - cht)/ np.cos(teta)

V_ht = [0.35, 0.5]
V_vt = [0.04, 0.06]

s_it = np.linspace(0,1,200)
Vht = list(); Sht_old = list()

for i, S_ht in enumerate(s_it):
    Vht_test = ((l_ht) * S_ht) / (c_medium * S)
    if (Vht_test >= V_ht[0] and Vht_test <= V_ht[1]):
        Vht.append(Vht_test)
        Sht_old.append(S_ht)
        
Sht_n = np.array(Sht_old)
c_ht = (Sht_n / AR) ** (1 / 2)
b_ht = (Sht_n / c_ht)

fig, ax = plt.subplots()

for i in range(0,len(b_ht)):
    ax = plt.plot([0, b_ht[i]], [0, 0]) 
    ax = plt.plot([b_ht[i], b_ht[i]], [0, c_ht[i]])
    ax = plt.plot([0, b_ht[i]], [c_ht[i], c_ht[i]]) 
    ax = plt.plot([0, 0], [0, c_ht[i]])

plt.axis('equal')

# Vvt = (l_vt * S_vt) / (b * S) 