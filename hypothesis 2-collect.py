# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:10:34 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:04:48 2020

@author: Yunfan Hong
"""


with open(r"C:\\Users\\Administrator\\Desktop\\normal.txt",mode="r",encoding="utf-8")as f:      #input your data file
    data = f.read()

a=[]        #cutting commit unit

a=data.split("\ncommit")
a.remove(a[0])


bug=[]
fix=[]
normal=[]
n1=0
n2=0
n3=0

for i in a:
    if "bug" in i:
        bug.append(i)
        n1+=1
        if n1 ==50:
            break
for i in a:
    if "fix" in i:
        fix.append(i)
        n2+=1
        if n2 ==50:
            break
for i in a:
    if "bug" not in i and "fix" not in i:
        normal.append(i)
        n3+=1
        if n3 ==50:
            break
#print(fix)
#
