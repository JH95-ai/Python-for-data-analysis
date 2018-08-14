#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
#Python最基本的时间序列类型就是以时间戳为索引的Series
dates=[datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),
       datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
ts=Series(np.random.randn(6),index=dates)
print(ts)
#这些datetime对象实际上是被放在一个DatetimeIndex中的.
# 现在，变量ts就成为一个TimeSeries了
print(type(ts))
print(type(ts.index))
#跟其他Series一样,不同索引的时间序列之间的算术运算会自动按时间对齐
print(ts+ts[::2])   #无法对齐的地方自动填充NA
#pandas用NumPy的datetime64数据类型以纳秒形式存储时间戳
print(ts.index.dtype)
#DatetimeIndex中的各个标量值是pandas的Timestamp对象
stamp=ts.index[0]
print(stamp)
#由于TimeSeries是Series的一个子类，
# 所以在索引以及数据选取方面它们的行为是一样的
stamp=ts.index[2]
print(stamp)
#传入一个可以被解释为日期的字符串
print(ts['1/10/2011'])
print(ts['20110110'])
#通过日期进行切片的方式只对规则Series有效
print(ts[datetime(2011,1,7):])
print(ts)
print(ts['1/6/2011':'1/11/2011'])#1/20不存在没关系，自动会查
print(ts.truncate(after='1/9/2011'))#最远到2011/1/9
