# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:39:21 2020

@author: 14110
"""

import time
t1=time.time()
with open(r"C:\\Users\\lirs1\\Desktop\\normal.txt",mode="r",encoding="utf-8")as f:      #input your data file
    data = f.read()

a=[]        #切割commit单元

a=data.split("Author: ")
a.remove(a[0])



hang=[]        #切割行
author={}        #作者
n=0
for i1 in a:        
    n+=1
    v0=0
    v2=0
    hang=i1.split("\n")

    if hang[0] not in author:
        v0=1
        if "fix" in i1:
            v2=1
        author[hang[0]]=[v0,v2]
    else:
        author[hang[0]][0]+=1
        if "fix" in i1:
            author[hang[0]][1]+=1
    hang=[]
    v0=0
    v2=0

#x轴bug y轴fix
amount=[]
fix=[]
bf=list(author.values())
for i in bf:
    amount.append(i[0])
    fix.append(i[1])
amount2 = []
for i in amount:
    temp = []
    temp.append(i)
    amount2.append(temp)
fix2 = []
for i in fix:
    temp2 = []
    temp2.append(i)
    fix2.append(temp2)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(amount2,fix2)
print("方程的确定性系数R的平方：",lm.score(amount2,fix2))
print("线性回归算法w值：",lm.coef_)
print("线性回归算法b值：",lm.intercept_)
fig = plt.figure()          #key and value as axis
plt.scatter(amount, fix, color='r', marker='+')
plt.plot(amount2,lm.predict(amount2),color = 'green',linewidth = 3)
plt.show()
t2=time.time()
print(t2-t1)











