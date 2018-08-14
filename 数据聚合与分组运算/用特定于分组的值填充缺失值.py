#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
s=Series(np.random.randn(6))
s[::2]=np.nan
#print(s)
a=s.fillna(s.mean())
#print(a)

#对不同的分组填充不同的值，只需要将数据分组，并使用apply和一个能够对各数据块调用
#fillna的函数即可
states=['Ohio','New York','Vermont','Florida',
        'Oregon','Nevada','California','Idaho']
group_key=['East']*4+['West']*4
data=Series(np.random.randn(8),index=states)
data[['Vermont','Nevada','Idaho']]=np.nan
print(data)

#用分组平均值去填充NA值
fill_mean=lambda g:g.fillna(g.mean())
a=data.groupby(group_key).apply(fill_mean)
print(a)
#此外，也可以在代码中预定义各组的填充值。由于分组具有一个name属性，
fill_values={'East':0.5,'West':-1}
fill_func=lambda g:g.fillna(fill_values[g.name])
b=data.groupby(group_key).apply(fill_func)
print(b)
