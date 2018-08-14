#-*-coding:utf-8-*-
from pandas import DataFrame
import numpy as np
df= DataFrame({'key1':['a','a','b','b','a'],
               'key2':['one','two','one','two','one'],
               'data1':np.random.randn(5),
               'data2':np.random.randn(5)})
#print(df)
grouped=df['data1'].groupby(df['key1'])
#print(grouped.mean())
means=df['data1'].groupby([df['key1'],df['key2']]).mean()
#print(means.unstack())
states=np.array(['Ohio','California','California','Ohio','Ohio'])
years=np.array([2005,2005,2006,2005,2006])
#print(df['data1'].groupby([states,years]).mean())
#print(df.groupby('key1').mean())
#print(df.groupby(['key1','key2']).mean())
#print(df.groupby(['key1','key2']).size())
#for name,group in df.groupby('key1'):
  #  print(name)
  #  print(group)
#for (k1,k2),group in df.groupby(['key1','key2']):
 #   print(k1,k2)
  #  print(group)
#pieces=dict(list(df.groupby('key1')))
#print(pieces['b'])
grouped=df.groupby(df.dtypes,axis=1)
#print(dict(list(grouped)))
print(df.groupby(['key1','key2'])[['data2']].mean())
s_grouped=df.groupby(['key1','key2'])['data2']
print(s_grouped.mean())
