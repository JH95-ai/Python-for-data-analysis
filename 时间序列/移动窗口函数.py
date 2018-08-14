#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame, Series
from scipy.stats import percentileofscore
close_px_all = pd.read_csv('/home/jethro/文档/pydata-book-master/data/stock_px.csv',
                           parse_dates=True,index_col=0)
close_px=close_px_all[['AAPL','MSFT','XOM']]
#在移动窗口上计算的各种统计函数也是一类常见于时间序列的数组变换
#移动窗口函数
#roll_mean是其中最简单的一个，它接受一个TimeSeries或DataFrame以及
#一个window（表示期数)
#close_px.AAPL.plot()
#close_px.rolling(window=250).mean().plot()
#plt.show()
#min_periods代表最少取10天的值
a=close_px.AAPL.rolling(window=250,min_periods=10).std()[:15]
print(a)
#close_px.AAPL.rolling(window=250,min_periods=10).std().plot()


#要计算扩展窗口平均，可以将扩展窗口看做一个特殊的窗口，其长度与时间序列一样
#通过rolling定义扩展平均
#对DataFrame取60天平均线
close_px.expanding(min_periods=60).mean().plot()
plt.show()


#指数加权函数

fig,axes=plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True,
                      figsize=(12,7))
aapl_px=close_px.AAPL['2005':'2009']
ma60=aapl_px.rolling(window=60).mean()
ewma60=aapl_px.ewm(span=60).mean()#ewm=指数加权
aapl_px.plot(style='k-',ax=axes[0])
ma60.plot(style='k--',ax=axes[0])
aapl_px.plot(style='k-', ax=axes[1])
ewma60.plot(style='k--', ax=axes[1])
axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially-weighted MA')

#二元移动窗口函数
spx_px=close_px_all['SPX']
spx_rets=spx_px/spx_px.shift(1)-1
returns = close_px.pct_change()
corr = returns.AAPL.rolling(window=125,min_periods=100).corr(spx_rets)
corr[95:105]
