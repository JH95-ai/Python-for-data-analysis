#-*-coding:utf-8-*-
from pandas import DataFrame
import numpy as np
df= DataFrame({'key1':['a','a','b','b','a'],
               'key2':['one','two','one','two','one'],
               'data1':np.random.randn(5),
               'data2':np.random.randn(5)})
grouped=df.groupby('key1')
#print(grouped['data1'].quantile(0.9))
#如果使用自己的聚合函数，只需要将其传入aggregate或agg方法即可
def peak_to_peak(arr):
    return arr.max()-arr.min()
#print(grouped.agg(peak_to_peak))
print(grouped.describe())
