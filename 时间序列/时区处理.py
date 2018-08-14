#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour,Minute
import pytz
#print(pytz.common_timezones[-5:])
#要从pytz中获取时区对象,使用pytz.timezone即可
tz=pytz.timezone('US/Eastern')
#print(tz)
#默认情况下，pandas中的时间序列是单纯的时区
rng=pd.date_range('3/9/2012 9:30',periods=6,freq='D')
ts=Series(np.random.randn(len(rng)),index=rng)
#其索引的tz字段为None
#print(ts.index.tz)
#在生成日期范围的时候还可以加上一个时区集
a=pd.date_range('3/9/2012 9:30',periods=10,freq='D',tz='UTC')
#print(a)
#从单纯到本地化的转换是通过tz_localize方法处理的
ts_utc=ts.tz_localize('UTC')
#print(ts_utc)
#print(ts_utc.index)
#一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到
#别的时区
#print(ts_utc.tz_convert('US/Eastern'))
#对于上面这个序列,可以将其本地化到EST，然后转换为UTC或柏林时间
ts_eastern=ts.tz_localize('US/Eastern')
#print(ts_eastern.tz_convert('UTC'))
#print(ts_eastern.tz_convert('Europe/Berlin'))
#tz_localize和tz_convert也是DatetimeIndex的实例方法
#print(ts.index.tz_localize('Asia/Shanghai'))

#操作时区意识型Timestamp对象
#跟时间序列和日期范围差不多，Timestamp对象也能被从单纯型本地化为时区
#意识型，并从一个时区转换到另一个时区
stamp=pd.Timestamp('2011-03-12 04:00')
stamp_utc=stamp.tz_localize('utc')
#print(stamp_utc.tz_convert('US/Eastern'))
#在创建Timestamp时，还可以传入一个时区信息
stamp_moscow=pd.Timestamp('2011-03-12 04:00',tz='Europe/Moscow')
#print(stamp_moscow)
#时区意识型Timestamp对象在内部保存了一个UTC时间戳值。这个UTC值在时区
#转换过程中是不会发生变化的
#print(stamp_utc.value)
#print(stamp_utc.tz_convert('US/Eastern').value)
#当使用pandas的DateOffset对象执行时间算术运算时，运算过程会自动关注
#是否存在夏令时转变期
#夏令时转变前30分钟

stamp=pd.Timestamp('2012-03-12 01:30',tz='US/Eastern')
print(stamp)
print(stamp+Hour())
#夏令时转变前90分钟
stamp=pd.Timestamp('2012-11-04 00:30',tz='US/Eastern')
print(stamp)
print(stamp +2*Hour())


#不同时区之间的运算
#如果两个时间序列的时区不同，在将它们合并到一起时，最终结果就会是UTC，
#由于时间戳其实是以UTC存储的，所以这是一个很简单的运算，
#并不需要发生任何转换
rng=pd.date_range('3/7/2012 9:30',periods=10,freq='B')
ts=Series(np.random.randn(len(rng)),index=rng)
print(ts)
ts1=ts[:7].tz_localize('Europe/London')
ts2=ts1[2:].tz_convert('Europe/Moscow')
result=ts1+ts2
print(result.index)
