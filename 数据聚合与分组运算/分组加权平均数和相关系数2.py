#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
close_px=pd.read_csv('/home/jethro/文档/pydata-book-master/data/stock_px.csv'
                     ,parse_dates=True,index_col=0  )
a=close_px[-4:]
#print(a)
rets=close_px.pct_change().dropna()
spx_corr=lambda x: x.corrwith(x['SPX'])
by_year=rets.groupby(lambda x:x.year)
b=by_year.apply(spx_corr)
#print(b)
#苹果和微软的年度相关系数
c=by_year.apply(lambda g:g['AAPL'].corr(g['MSFT']))
print(c)
