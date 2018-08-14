#-*-coding:utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import numpy as np
macro=pd.read_csv('/home/jethro/文档/pydata-book-master/data/macrodata.csv')
data=macro[['cpi','m1','tbilrate','unemp']]
trans_data=np.log(data).diff().dropna()
plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title('Changes in log %s vs. log %s' %('m1','unemp'))
pd.scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.3)
plt.show()
