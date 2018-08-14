#-*-coding:utf-8-*-
import numpy as np
import pandas as pd
from datetime import time
from pandas import DataFrame, Series

#时间序列以及截面对齐
#pandas可以在算术运算中自动对齐数据，
close_px_all=pd.read_csv('/home/jethro/文档/pydata-book-master/data/stock_px.csv',
                         parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM', 'IBM', 'SPX']]
#print(close_px.head())
#print(close_px.tail())
volume_all = pd.read_csv('/home/jethro/文档/pydata-book-master/data/volume.csv', parse_dates=True, index_col=0)
volume = volume_all[['AAPL', 'MSFT', 'XOM', 'SPX']]
#print(volume.head())

#由于pandas会在算术运算过程中自动将数据对齐，并在sum这样的函数中排除
#缺失数据
#自动匹配对应位置，计算当天成交所额，IBM没有就填充NA
#print((close_px*volume).head())
vwap=(close_px*volume).sum()/volume.sum()
#print(vwap)
#print(vwap.dropna())

#如果手工进行对齐，可以使用DataFrame的align方法，它返回的是一个元组
#含有两个对象的重索引版本
tp=close_px.align(volume,join='inner')
#返回的是与volume对齐的元组
#tp[0]是close_px，tp[1]是volume
print(tp[0][:10])
print(tp[1][:10])

#另一个不可或缺的功能，通过一组索引可能不同的Series构建一个DataFrame
s1=Series(range(3),index=['a','b','c'])
s2=Series(range(4),index=['a','b','c','e'])
s3=Series(range(3),index=['f','a','c'])
df=DataFrame({'one':s1,'two':s2,'three':s3})
print(df)

#跟前面一样，这里也可以显式定义结果的索引(丢弃其余的数据)
#显示定义索引
df2=DataFrame({'one':s1,'two':s2,'three':s3},index=list('face'))
print(df2)


#频率不同的时间序列的运算
#频率转换和重对齐的两大主要工具是resample和reindex方法
#resample用于将数据转换到固定频率
#reindex则用于使数据符合一个新索引,它们都支持插值(如前向填充)逻辑
ts1=Series(np.random.randn(3),
           index=pd.date_range('2012-6-13',periods=3,freq='W-WED'))
print(ts1)

#如果将其重采样到工作日(星期一到星期五)频率，则那些没有数据的日子就会出现
#一个‘空洞’
#重新采样，如果没有ffill，就用ts2.iteritems()遍历访问
ts1=ts1.resample('B').ffill()
print(ts1)

#在实际工作当中,将较低频率的数据升采样到较高的规整频率是一种不错的解决方案
#但是对于更一般化的不规整时间序列可能就不太合适了.
dates = pd.DatetimeIndex(['2012-6-12',
                          '2012-6-17',
                          '2012-6-18',
                          '2012-6-21',
                          '2012-6-22',
                          '2012-6-29'])
ts2 = Series(np.random.randn(6), index=dates)
print(ts2)
#如果将ts1中最当前的值加到ts2上。一个办法是将两者重采样为规整频率后再相加
#但是如果想维持ts2中的日期索引，则reindex会是更好的一种解决方案

i=ts1.reindex(ts2.index,method='ffill')
print(i)
#ts1的索引先和ts2的索引对齐，然后相加
j=ts2+ts1.reindex(ts2.index,method='ffill')
print(j)

gdp = Series([1.78, 1.94, 2.08, 2.01, 2.15, 2.31, 2.46],
index=pd.period_range('1984Q2', periods=7, freq='Q-SEP'))
print(gdp)

infl = Series([0.025, 0.045, 0.037, 0.04],
              index=pd.period_range('1982', periods=4, freq='A-DEC'))
print(infl) # 显然和gdp的时间频率不一样"

#跟timestamp的时间序列不同，由period索引的两个不同频率的时间序列之间
#必须进行显式转换

#调整季度
infl_q=infl.asfreq('Q-SEP',how='end')
print(infl_q)
#索引匹配并填充缺失值
k=infl_q.reindex(gdp.index,method='ffill')
print(k)


#时间和最当前数据提取
rng = pd.date_range('2012-06-01 09:30', '2012-06-01 15:59', freq='T')
# 交易时段按分钟采样
rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 4)])
# 再补4天
ts = Series(np.arange(len(rng), dtype=float), index=rng)
print(ts.head())
print(ts.tail())
#利用python的datetime.time对象进行索引即可抽取出这些时间点上的值
print(ts[time(10,0)])#抽取10点的数据
print(ts.at_time(time(10,0)))
#between_time方法，它用于选取两个Time对象之间的值
j=ts.between_time(time(10,0),time(10,1))#定位到时间段
print(j)

#如果刚好没有数据落在某个具体时间上,希望得到上午10点之前最后出现的值
#根据ts随机选个排列，并选择700条及以后的数据进行排序
indexer=np.sort(np.random.permutation(len(ts))[700:])
irr_ts=ts.copy()
#根据随机下标索引把一部分时间点数据设置为NA
irr_ts[indexer]=np.nan
print(irr_ts['2012-06-01 09:50':'2012-06-01 10:00'])
#如果将一组Timestamp传入asof方法,就能得到这些时间点处的有效值
#连续四个工作日的上午10点
selection=pd.date_range('2012-06-01 10:00',periods=4,freq='B')
#上面随机几次,确保某个10点数据为NA.asof的话会拿最近数据填充
irr_ts.asof(selection)

#拼接多个数据源
data1 = DataFrame(np.ones((6, 3), dtype=float),
                  columns=['a', 'b', 'c'],
                  index=pd.date_range('6/12/2012', periods=6))
data2 = DataFrame(np.ones((6, 3), dtype=float) * 2,
                 columns=['a', 'b', 'c'],
                  index=pd.date_range('6/13/2012', periods=6))
spliced = pd.concat([data1.loc[:'2012-06-14'], data2.loc['2012-06-15':]])
# 默认纵向连接
print(spliced)

#假设data1缺失了data2中存在的某个时间序列
data2 = DataFrame(np.ones((6, 4), dtype=float) * 2,
                  columns=['a', 'b', 'c', 'd'],
                  index=pd.date_range('6/13/2012', periods=6))
spliced = pd.concat([data1.loc[:'2012-06-14'], data2.loc['2012-06-15':]])
print(spliced) # data1没有d列"

#combine_first可以引入合并点之前的数据，这样也就扩展了‘d’项的历史
#用data2的每一行对应列上的值去填充NA
spliced_filled=spliced.combine_first(data2)
print(spliced_filled)

#DataFrame也有一个类似的方法update,可以实现就地更新.如果只想填充空洞，则必须传入
#overwrite=False才行
spliced.update(data2,overwrite=False)
print(spliced)

#上面这些技术都可实现将数据中的符号替换为实际数据
#但有时利用DataFrame的索引机制直接对列进行设置会更简单一些
cp_spliced=spliced.copy()
#data1没有18号数据
cp_spliced[['a','c']]=data1[['a','c']]
print(cp_spliced)

#收益值数以及累计收益
close_px_all = pd.read_csv('/home/jethro/文档/pydata-book-master/data/stock_px.csv', parse_dates=True, index_col=0)
# 重新读取数据\n",
close_px = close_px_all[['AAPL', 'MSFT', 'XOM', 'IBM', 'SPX']]
price=close_px['AAPL']
print(price.tail())
# 计算回报率
pro=price['2011-10-03'] / price['2011-3-01'] - 1
print(pro)

df=DataFrame({'close_price':price})
print(df.tail())

returns=df.pct_change()['close_price']
print((1+returns).head())
