#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
from pandas.tseries.offsets import Hour,Minute,Day,MonthEnd
import pytz
#时期表示的是时间区间,比如数日，数月，数系，数年等.Period类所表示的就是
#这种数据类型，其构造函数需要用到一个字符串或整数
p=pd.Period(2007,freq='A-DEC')
#print(p)
#这个Period对象表示的是从2007年1月1日到2007年12月31日之间的
#整段时间。只需对Period对象加上或减去一个整数即可达到根据其频率进行位移
#的效果
print(p+5)
print(p-2)
#如果两个Period对象拥有相同的效率，则它们的差就是它们之间的单位数量
a=pd.Period('2014',freq='A-DEC')-p
print(a)
#period_range函数可用于创建规则的时期范围
rng=pd.period_range('1/1/2000','6/30/2000',freq='M')
print(rng)
#PeriodIndex类保存了一组Period，它可以在任何pandas数据结构中被用作
#轴索引
b=Series(np.random.randn(6),index=rng)
print(b)
#PeriodIndex类的构造函数允许直接使用一组字符串
values=['2001Q3','2002Q2','2003Q1']
index=pd.PeriodIndex(values,freq='Q-DEC')
print(index)


#Period和PeriodIndex对象都可以通过其astreq方法被转换成别的频率。

#年度时期，将其转换为当年年初或年末的一个月度时期
p=pd.Period('2007',freq='A-DEC')
c=p.asfreq('M',how='start')
print(c)
d=p.asfreq('M',how='end')
print(d)
#将Period('2007',freq='A-DEC')看作一个被划分为多个月度时期的时间段中
#的游标
p=pd.Period('2007',freq='A-JUN')
#截至到2007/6/30的一年时间
e=p.asfreq('M','start')
print(e)
f=p.asfreq('M','end')
print(f)


#pandas支持12种可能的季度型频率，即Q-JAN到Q-DEC
#按季度计算的时间频率
#Q代表季度为单位（开始时间要减去1个季度，Q4请忽略，这里没卵用）
#JAN代表1月，结合Q，取1/31
i=pd.Period('2012Q4',freq='Q-JAN')
print(i)
#在以1月结束的财年中，2012Q4是从11月到1月
print(i.asfreq('D','start'))
print(i.asfreq('D','end'))
#获取该季度倒数第二个工作日下午4点的时间戳
p4pm=(i.asfreq('B','e')-1).asfreq('T','s')+16*60
print(p4pm)
print(p4pm.to_timestamp())
#period_range还可用于生成季度型范围
#以Q为单位
rngb=pd.period_range('2011Q3','2012Q4',freq='Q-JAN')
ts=Series(np.arange(len(rngb)),index=rngb)
print(ts)
#频率变成分钟,再加16小时
#最后一个工作日减1的下午4点
new_rngb=(rngb.asfreq('B','e')-1).asfreq('T','s')+16*60
ts.index=new_rngb.to_timestamp()
print(ts)

#将Timestamp转换为Period(及其反向过程)
#通过使用to_period方法，可以将时间戳索引的Series和DataFrame对象
#转换为以时期索引
rngc=pd.date_range('1/1/2000',periods=3,freq='M')
print(rngc)
tsc=Series(np.random.randn(3),index=rngc)
print(tsc)
pts=tsc.to_period()
print(pts)

rngd=pd.date_range('1/29/2000',periods=6,freq="D")
ts3=Series(np.random.randn(6),index=rngd)
print(ts3.to_period('M'))
#要转换为时间戳，使用to_timestamp即可
pts=ts3.to_period()
print(pts)
print(pts.to_timestamp(how='end'))

data=pd.read_csv('/home/jethro/文档/pydata-book-master/data/macrodata.csv')
print(data.year)
print(data.quarter)
#将这两个数组以及一个频率传入PeriodIndex，就可以将它们合并成DataFrame的一个索引
index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
print(index)



