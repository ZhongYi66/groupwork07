import numpy as np
import pandas as pd
from pandas import DataFrame

df = pd.read_csv("data_v4.4",comment="#",header=0,sep=" ",index_col="lv",columns=["hour","bugs"])

s = df['hour']
j = 0
l = []
for i in s:
    b = s[j+1]-s[j]
    j = j+1
    l.append(b)
    if j > len(s):
        break

df.append(l)