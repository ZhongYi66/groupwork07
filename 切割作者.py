# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 17:34:48 2020

@author: 14110
"""

'''
#把600+M文件存储为可打开格式
f = open("C:\\Users\\14110\\Desktop\\789.txt", 'r', encoding='utf-8', errors='ignore')  # 打开要处理的文件
data = open("C:\\Users\\14110\\Desktop\\normal1.txt", 'w+', encoding='utf-8')
lines = f.readlines()
for lines in lines:  # 对TXT 进行逐行读取
    print(lines, file=data)

'''
with open(r"C:\\Users\\14110\\Desktop\\normal.txt",mode="r",encoding="utf-8")as f:      #input your data file
    data = f.read()

a=[]
a=data.split("commit")

n=0
for i in a:
    if "maintain" in i:
        n+=1
print(n)







