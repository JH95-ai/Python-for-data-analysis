#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
people=DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],index=['Joe','Steve','Wes','Jim','Travis'])
people.ix[2:3,['b','c']]=np.nan
#print(people)
mapping={'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
by_column=people.groupby(mapping,axis=1)
#print(by_column.sum())
#Series进行分组
map_series=Series(mapping)
#print(map_series)
#print(people.groupby(map_series,axis=1).count())
#函数进行分组
#print(people.groupby(len).sum())
key_list=['one','one','one','two','two']
print(people.groupby([len,key_list]).min())