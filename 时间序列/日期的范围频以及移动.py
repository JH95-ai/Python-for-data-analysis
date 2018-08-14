#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour,Minute

dates=[datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),
       datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
ts=Series(np.random.randn(6),index=dates)
a=ts.resample('D')
#print(a)
#pandas.date_range可用于生成指定长度的DatatimeIndex
index=pd.date_range('4/1/2012','6/1/2012')
#print(index)
#默认情况下，date_range会产生按天计算的时间点.如果只传入起始或结束日期
#那就还得传入一个表示一段时间的数字
b=pd.date_range(start='4/1/2012',periods=20)
#print(b)
c=pd.date_range(end='6/1/2012',periods=20)#20天方向向前
#print(c)
#起始和结束日期定义了日期索引的严格边界.例如，如果你想要生成一个由每月最后一个工作日
#组成的日期索引，可以传入'BM'频率，这样就只会包含时间间隔内符合频率要求的日期
d=pd.date_range('1/1/2000','12/1/2000',freq='BM')
#print(d)#BM=business end of month 结果调整到月底
#date_range默认会保留起始和结束时间戳的时间信息
e=pd.date_range('5/2/2012 12:56:31',periods=5)#时分秒保留
#print(e)
#虽然起始和结束日期带有时间信息，但希望产生一组被规范化到午夜的时间戳.
#normalize选项即可实现该功能
f=pd.date_range('5/2/2012 12:56:31',periods=5,normalize=True)
#时分秒被和谐
#print(f)
#pandas中的频率是由一个基础频率和一个乘数组成的.基础频率通常都以一个字符
#别名表示，比如‘M’表示每月，'H'表示每小时.对于每个基础频率，都有一个被
#称为日期偏移量的对象与之对应。例如，按小时计算的频率可以用Hour类表示
hour=Hour()
#print(hour)
#传入一个整数即可定义偏移量的倍数
four_hours=Hour(4)
#print(four_hours)
#只需使用诸如H或4H这样的字符串别名即可.在基础频率前面放上一个整数即可
#创建倍数
a=pd.date_range('1/1/2000','1/3/2000 23:59',freq='4h')
#以4小时为间隔单位，两边闭区间.
#print(a)
#大部分偏移量对象都可通过加法进行连接
b=Hour(2)+Minute(30)
#print(b)
#同理,也可以传入频率字符串，这种字符串可以被高效得解析为等效的表达式
c=pd.date_range('1/1/2000',periods=10,freq='2h30min')
#print(c)
#WOW是一种非常实用的频率类,它以WOM开头。它使你能获得诸如'每月第3个星期五
# 之类的日期
rng=pd.date_range('1/1/2012','9/1/2012',freq='WOM-3FRI')
#每月第三个周五
#print(rng)
#移动指的是沿着时间轴将数据前移或后移.
# Series和DataFrame都有一个shift方法用于执行单纯的前移或后移操作，
#保持索引不变
ts=Series(np.random.randn(4),
          index=pd.date_range('1/1/2000',periods=4,freq='M'))
#print(ts)
#数据整体往后推2步，key不动
#print(ts.shift(2))
#数据整体向前推2步，key不动
#print(ts.shift(-2))
#shift通常用于计算一个时间序列或多个时间序列中的百分比变化
f=ts.shift(1)-1
#print(f)
#由于单纯的移位操作不会修改索引，所以部分数据会被丢弃.
#因此，如果频率已知，则可以将其传给shift以便实现对时间戳进行位移
#而不是对数据进行简单位移
g=ts.shift(2,freq='M')
#print(g)
i=ts.shift(3,freq='D')
#print(i)

#pandas的日期偏移量还可以用在datetime或Timestamp对象上
from pandas.tseries.offsets import Day,MonthEnd
now=datetime(2011,11,17)
#print(now+3*Day())
#如果加的是锚点偏移量，第一次增量会将原日期向前滚动到符合频率规则的
#下一个日期
#print(now+MonthEnd())
#通过锚点偏移量的rollforward和rollback方法，可显式的将日期向前或向后
#滚动
offset=MonthEnd()
#print(offset.rollforward(now))
#print(offset.rollback(now))
#日期偏移量还有一个巧妙的用法，即结合groupby使用这两个'滚动'方法
ts=Series(np.random.randn(20),index=pd.date_range('1/15/2000'
        ,periods=20,freq='4d'))
print(ts.groupby(offset.rollforward).mean())
print(ts.resample('M',how='mean'))

