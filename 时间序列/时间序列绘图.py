#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
from pandas import DataFrame, Series
close_px_all = pd.read_csv('/home/jethro/文档/pydata-book-master/data/stock_px.csv',
                           parse_dates=True,index_col=0)
close_px=close_px_all[['AAPL','MSFT','XOM']]
close_px=close_px.resample('B',fill_method='ffill')
print(close_px)
#close_px['AAPL'].plot()
#当对DataFrame调用plot时,所有时间序列都会被绘制在一个subplot上，
#并有一个图例说明哪个是哪个
#close_px.ix['2009'].plot()

#苹果公司在2011年1月到3月间的每日股价
#['AAPL'].ix['01-2011':'03-2011'].plot()
#plt.show()


#季度型频率的数据会用季度标记进行格式化
appl_q=close_px['AAPL'].resample('Q-DEC').ffill()
appl_q.loc['2009':].plot()
plt.show()