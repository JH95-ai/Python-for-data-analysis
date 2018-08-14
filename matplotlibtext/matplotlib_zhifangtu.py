#-*-coding:utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import csv
tips=pd.read_csv('/home/jethro/文档/pydata-book-master/data/tips.csv')
tips['tip_pct']=tips['tip']/tips['total_bill']
tips['tip_pct'].hist(bins=50)
tips['tip_pct'].plot(kind='kde')
plt.show()
