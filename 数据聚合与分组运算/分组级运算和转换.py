#-*-coding:utf-8-*-
from pandas import DataFrame
import pandas as pd
import numpy as np
df= DataFrame({'key1':['a','a','b','b','a'],
               'key2':['one','two','one','two','one'],
               'data1':np.random.randn(5),
               'data2':np.random.randn(5)})
k1_means=df.groupby('key1').mean().add_prefix("mean_")
#print(k1_means)
k1_means_p=pd.merge(df,k1_means,left_on='key1',right_index=True)
#print(k1_means_p)
#在GroupBy上使用transform方法
people=DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],
                 index=['Joe','Steve','Wes','Jim','Travis'])
key=['one','two','one','two','one']
a=people.groupby(key).mean()
#print(a)
b=people.groupby(key).transform(np.mean)
#print(b)
def demean(arr):
    return arr-arr.mean()
demeaned=people.groupby(key).transform(demean)
a=demeaned.groupby(key).mean()
print(a)
#print(demeaned)
