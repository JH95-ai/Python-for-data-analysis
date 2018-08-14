#-*-coding:utf-8-*- 
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
now=datetime.now()
#print(now)
#print(now.year,now.month,now.day)
#datetime以毫秒形式存储日期和时间.
# datetime.timedelta表示两个datetime对象之间的时间差
delta=datetime(2011,1,7)-datetime(2008,6,24,8,15)
#print(delta)
#print(delta.days)
#print(delta.seconds)
#给datetime对象加上一个或多个timedelta,这样会产生一个新对象
start=datetime(2011,1,7)
a=start+timedelta(12)
#print(a)
#利用str或strftime方法
# datetime对象和pandas的Timestamp对象可以被格式化为字符串
stamp=datetime(2011,1,3)
#print(str(stamp))#默认格式转换
#print(stamp.strftime("%Y-%m-%d"))#指定格式转换
value='2011-01-03'
a=datetime.strptime(value,'%Y-%m-%d')
print(a)
datestrs=['7/6/2011','8/6/2011']





