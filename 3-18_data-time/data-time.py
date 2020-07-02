# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:34:48 2020

@author: 14110
"""

with open(r"C:\Users\14110\Desktop\date.txt","r")as f:      #input your data file
    data = f.read()

a=[]                    #cut the str
a=data.split("\n")  

b=[]
for i in a:             #extract the date
    if len(i)==30:
        b.append(i[4]+i[5]+i[6]+" "+i[8]+i[9]+" "+i[20]+i[21]+i[22]+i[23])
    else:
        b.append(i[4]+i[5]+i[6]+" "+i[8]+" "+i[19]+i[20]+i[21]+i[22])

from collections import Counter
c = Counter(b)          #creat a date dictionary

vk = list(c.keys())     #separately store the key and value
vk.reverse()
vl = list(c.values())
vl.reverse()

import matplotlib.pyplot as plt

fig = plt.figure()          #key and value as axis
plt.scatter(vk, vl, color='r', marker='+')
plt.xticks(vk[::1300])
plt.show()          #draw the figure




