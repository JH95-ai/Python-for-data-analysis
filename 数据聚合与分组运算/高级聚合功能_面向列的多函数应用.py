#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
tips=pd.read_csv('/home/jethro/文档/pydata-book-master/data/tips.csv')
#添加‘小费占总额百分比’的列
tips['tip_pct']=tips['tip']/tips['total_bill']
#print(tips[:6])
grouped=tips.groupby('smoker')
#grouped_pct=grouped['tip_pct']
#print(grouped_pct.agg('mean'))
#如果传入的是一个由（name,function）元组组成的列表
# ，则各元组的第一个元素就会被用作DataFrame的列名
functions=['count','mean','max']
result=grouped['tip_pct','total_bill'].agg(functions)
#print(result['tip_pct'])
ftuples=[('Durchschnitt','mean'),('Abweichung',np.var)]
#print(grouped['tip_pct','total_bill'].agg(ftuples))
#print(grouped.agg({'tip':np.max,'size':'sum'}))
print(grouped.agg({'tip_pct':['min','max','mean','std'],'size':sum}))