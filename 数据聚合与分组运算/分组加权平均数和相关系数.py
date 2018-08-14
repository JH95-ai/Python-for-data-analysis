#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
df=DataFrame({'category':['a','a','a','a','b','b','b','b'],
              'data':np.random.randn(8),
              'weights':np.random.rand(8)})
#利用category计算分组加权平均数
grouped=df.groupby('category')
get_wavg=lambda g:np.average(g['data'],weights=g['weights'])
a=grouped.apply(get_wavg)
print(a)
