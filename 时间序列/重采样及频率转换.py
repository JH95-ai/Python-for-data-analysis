#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour,Minute,Day,MonthEnd
import pytz

#重采样指的是将时间序列从一个频率转换到另一个频率的处理过程.
#将高频率数据聚合到低频率称为降采样，而将低频率数据转换到高频率则称为升采样
#将W-WED（每周三）转换为W-FRI既不是降采样也不是升采样

#pandas对象都带有一个resample方法，它是各种频率转换工作的主力函数
rng=pd.date_range('1/1/2000',periods=100,freq='D')
ts=Series(np.random.randn(len(rng)),index=rng)
a=ts.resample('M',how='mean')
#print(a)
#统计每月平均数，实际上是根据月份做了group
b=ts.resample('M',how='mean',kind='period')
#print(b)


#在用resample对数据进行降采样时，需要考虑两样东西
#各区间哪边是闭合的
#如何标记各个聚合面元，用区间的开头还是末尾
rng=pd.date_range('1/1/2000',periods=12,freq='T')#T是按分钟
ts=Series(np.arange(12),index=rng)
print(ts)

#通过求和的方式将这些数据聚合到‘5分钟’块中
b=ts.resample('5min',how='sum')
print(b)
#默认情况下，面元的右边界是包含的，因此00：00到00：05的区间中是包含00：05的
#传入closed=‘left’会让区间以左边界闭合
c=ts.resample('5min',how='sum',closed='left',label='left')

print(c)
#从右边界减去一秒以便容易明白该时间戳到底表示的是哪个区间
#只需要通过loffset设置一个字符串或日期偏移量即可实现这个目的
d=ts.resample('5min',how='sum',loffset='-1s')
print(d)


#OHLC重采样
#金融领域有一种无所不在的时间序列聚合方式，即计算各面元的四个值：
#第一个值（open，开盘），最后一个值（close，收盘）
#最大值（high，最高），最小值（low，最低）
#传入how='ohlc'即可得到一个含有这四种聚合值的DataFrame
#整个过程十分高效，只需要一次扫描即可计算结果
e=ts.resample('5min',how='ohlc')#其实就是5分钟的K线图
print(e)

#另一种降采样的办法是使用pandas的groupby功能.例如，打算根据
#月份或星期几进行分组，只需传入一个能够访问时间序列的索引上的这些字段的
#函数即可
rng=pd.date_range('1/1/2000',periods=100,freq='D')
tsb=Series(np.arange(100),index=rng)
f=tsb.groupby(lambda x:x.month).mean()
print(f)
g=tsb.groupby(lambda x :x.weekday).mean()
print(g)

#将数据从低频率转换到高频率时,就不需要聚合了.
frame=DataFrame(np.random.randn(2,4),
                index=pd.date_range('1/1/2000',periods=2,freq='W-WED'),
                columns=['Colorado','Texas','New York','Ohio'])
print(frame[:5])

#将其重采样到日频率,默认会引入缺失值
df_daily=frame.resample('D')
#注意警告信息，resample现在生成的是一个延迟计算对象
print(df_daily)
#for i in df_daily.iteritems():
  #  print(i)


#对那些使用时期索引的数据进行重采样是件非常简单的事情
frames = DataFrame(np.random.randn(24, 4),
                  index=pd.period_range('1-2000', '12-2001', freq='M'),
                  columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(frames.head())

annual_frame=frame.resample('A-DEC',how='mean')
print(annual_frame)

#升采样要麻烦。必须决定在新频率中各区间的哪端用于放置原来的值
#与asfreq相像，convention参数默认为'end',可设置为'start'
i=annual_frame.resample('Q-DEC',fill_method='ffill')
print(i)
