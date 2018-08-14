#-*-coding:utf-8-*-
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame,Series
import pandas as pd
stamp=datetime(2011,1,3)
print(str(stamp))#默认格式切换
#print(stamp.strftime('%Y-%m-%d'))#指定转换格式
value='2011-01-03'
#print(datetime.strptime(value,'%Y-%m-%d'))
datestrs=['7/6/2011','8/6/2011']
data=[datetime.strptime(x,'%m/%d/%Y') for x in datestrs]
print(data)
#datetime.strptime是通过已知格式进行日期解析的最佳方式.但是每次都要编写格式定义是很麻烦的事情，尤其是对于一些常见的日期格式.
# 这种情况下，你可以用dateutil这个第三方包中的parser.parse方法
parse('2011-01-03')#自动解析，默认月在前
#dateutil可以解析几乎所有人类能够理解的日期表示形式
print(parse('Jan 31,1997 10:45 PM'))
#在国际通用的格式中，日通常出现在月的前面
#传入dayfirst=True即可解决这个问题
print(parse('6/12/2011',dayfirst=True))#日在月前
#pandas通常是用于处理成组日期的，不管这些日期是DataFrame的轴索引还是
#列，to_datetime方法可以解析多种不同的日期表示形式.对标准日期格式的
#解析非常快
print(datestrs)
a=pd.to_datetime(datestrs)
print(a)#变成时间索引对象
#它还可以处理缺失值
idx=pd.to_datetime(datestrs+[None])
print(idx)
print(idx[2])
b=pd.isnull(idx)
print(b)

