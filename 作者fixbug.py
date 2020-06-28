# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:39:21 2020

@author: 14110
"""

import time
t1=time.time()
with open(r"C:\\Users\\14110\\Desktop\\normal.txt",mode="r",encoding="utf-8")as f:      #input your data file
    data = f.read()

a=[]        #切割commit单元

a=data.split("Author: ")
a.remove(a[0])



hang=[]        #切割行
author={}        #作者
n=0
for i1 in a:        
    n+=1
    v1=0
    v2=0
    
    hang=i1.split("\n")

    if hang[0] not in author:
        if "bug" in i1:
            v1=1
        if "fix" in i1:
            v2=1
        author[hang[0]]=[v1,v2]
    else:
        if "bug" in i1:
            author[hang[0]][0]+=1
        if "fix" in i1:
            author[hang[0]][1]+=1      
    hang=[]
    v1=0
    v2=0


#x轴bug y轴fix
bug=[]
fix=[]
bf=list(author.values())


for i in bf:
    bug.append(i[0])
    fix.append(i[1])   

import matplotlib.pyplot as plt
fig = plt.figure()          #key and value as axis
plt.scatter(bug, fix, color='r', marker='+')
plt.show() 
print(len(author))

t2=time.time()
print(t2-t1)











