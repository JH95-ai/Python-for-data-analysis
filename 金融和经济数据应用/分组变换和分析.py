#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string
import tushare as ts
from pandas import DataFrame, Series
from pandas.tseries.offsets import Day, Hour, Minute, MonthEnd
from sklearn.linear_model import LinearRegression

#随机生成1000个股票代码,显示前10个
N=1000
def rangs(n):
    choices=string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in range(n)])
tickers=np.array([rangs(5) for _ in range(N)])
print(tickers[:10])
#创建一个含有3列的DataFrame来承载这些假想数据
M=500
df=DataFrame({'Monmentum':np.random.randn(M)/200+0.03,
              'Value':np.random.randn(M)/200+0.08,
              'ShortInterest':np.random.randn(M)/200-0.02},
             index=tickers[:M])
print(df.head())

#随机给公司分类，Financial或tech
ind_names=np.array(['FINANCIAL','TECH'])
sampler=np.random.randint(0,len(ind_names),N)
industries=Series(ind_names[sampler],
                  index=tickers,
                  name='industry')
print(industries.head())
#现在，就可以根据行业分类进行分组并执行分组聚合和变换了
by_industry=df.groupby(industries)
#计算按行分组的平均值
print(by_industry.mean())
print(by_industry.describe())
#行业内标准化过程
def zscore(group):
    # 每个股票减去所在组的平均值再除以标准差
    return (group-group.mean())/group.std()
#这样处理后，各行业的平均值为0，标准差为1
df_stand=by_industry.apply(zscore)
print(df_stand.head())
a=df_stand.groupby(industries).agg(['mean','std'])
print(a)
#显然均值为0，标准差为1
#rank内置变换函数
ind_rank=by_industry.rank(ascending=False)
b=ind_rank.groupby(industries).agg(['min','max'])
print(b)
#在股票投资组合的定量分析中,'排名和标准化'是一种很常见的变换运算组合,通过将rank和zscore
#链接在一起即可完成整个变换过程
#行业内排名和标准化
#标准化排名顺序
c=by_industry.apply(lambda x:zscore(x.rank()))
print(c.head())

#分组因子暴露
fac1,fac2,fac3 = np.random.rand(3, 1000)
ticker_subset = tickers.take(np.random.permutation(N)[:1000])
ticker_subset[:10]
factors = DataFrame({'f1': fac1, 'f2': fac2, 'f3': fac3},
                        index=ticker_subset)
print(factors.head())
port = Series(0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + np.random.rand(1000),
                 index=ticker_subset)
#相关系数
i=factors.corrwith(port)
print(i)

