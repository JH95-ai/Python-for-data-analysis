#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
#pandas 有一些能根据指定面元或样本分位数将数据拆分成多块的工具（如cut和qcut）.将这些函数跟groupby结合起来
#就能非常轻松地实现对数据集的桶（bucket）或分位数（quantile）分析了
frame=DataFrame({'data1':np.random.randn(1000),
                 'data2':np.random.randn(1000)})
factor=pd.cut(frame.data1,4)
#print(factor[:10])
#由cut返回的Factor对象可直接用于groupby
def get_stats(group):
    return {'min':group.min(),'max':group.max(),
            'count':group.count(),'mean':group.mean()}
grouped=frame.data2.groupby(factor)
a=grouped.apply(get_stats).unstack()
#print(a)

#要根据样本分位数得到大小相等的桶,使用qcut即可。传入labels=False即可只获取分位数的编号
grouping=pd.qcut(frame.data1,10,labels=False)
grouped=frame.data2.groupby(grouping)
b=grouped.apply(get_stats).unstack()
print(b)
