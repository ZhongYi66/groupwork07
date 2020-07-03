# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:04:48 2020

@author: Yunfan Hong
"""

import time
t1=time.time()
with open(r"C:\\Users\\Administrator\\Desktop\\normal.txt",mode="r",encoding="utf-8")as f:      #input your data file
    data = f.read()

a=[]        #cuing commit unit

a=data.split("Author: ")
a.remove(a[0])



hang=[]        #cutting line
author={}        #author
n=0
for i1 in a:        
    n+=1
    v0=0
    v1=0
    v2=0
    v3=0
    
    hang=i1.split("\n")

    if hang[0] not in author:
        v0=1
        if "bug" in i1:
            v1=1
        if "fix" in i1:
            v2=1
        if "maintain" in i1:
            v3=1
        author[hang[0]]=[v0,v1,v2,v3]
    else:
        author[hang[0]][0]+=1
        if "bug" in i1:
            author[hang[0]][1]+=1
        if "fix" in i1:
            author[hang[0]][2]+=1
        if "maintain" in i1:
            author[hang[0]][3]+=1
    hang=[]
    v1=0
    v2=0


#x-axis bug y-axis fix
amount=[]
bug=[]
fix=[]
maintain=[]
bf=list(author.values())


for i in bf:
    amount.append(i[0])
    bug.append(i[1])
    fix.append(i[2])   
    maintain.append(i[3])
    
import matplotlib.pyplot as plt

fig = plt.figure()          #key and value as axis


plt.scatter(bug, fix, color='r', marker='+')

plt.show() 
print(len(author))

t2=time.time()
print(t2-t1)
