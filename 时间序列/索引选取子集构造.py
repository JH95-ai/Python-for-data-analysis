#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
#由于TimeSeries是Series的一个子类，
# 所以在索引以及数据选取方面它们的行为是一样的
#对于较长的时间序列,只需传入'年'或'年月'即可轻松选取数据的切片
longer_ts=Series(np.random.randn(1000),
                 index=pd.date_range('1/1/2000',periods=1000))
print(longer_ts)#连续1000天的数据
print(longer_ts['2001'])
print(longer_ts['2001-05'])
dates=pd.date_range('1/1/2000',periods=100,freq='W-WED')
long_df=DataFrame(np.random.randn(100,4),index=dates,
                  columns=['Colorado','Texas','New York','Ohio'])
print(long_df.ix['5-2001'])
#带有重复索引的时间序列
dates=pd.DatetimeIndex(['1/1/2000','1/2/2000','1/2/2000',
                        '1/2/2000','1/3/2000'])
dup_ts=Series(np.arange(5),index=dates)
print(dup_ts)
#通过检查索引的is_unique属性,我们就知道他是不是唯一的
print(dup_ts.index.is_unique)
#对这个时间序列进行索引，要么产生标量值，要么产生切片，
# 具体要看所选的时间点是否重复
print(dup_ts['1/3/2000'])#不重复
print(dup_ts['1/2/2000'])#重复
#假设想要对具有非唯一时间戳的数据进行聚合.一个办法是使用groupby，
# 并传入level=0
grouped=dup_ts.groupby(level=0)
print(grouped.mean())
print(grouped.count())
