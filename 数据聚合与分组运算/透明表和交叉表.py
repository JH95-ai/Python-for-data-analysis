#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
tips=pd.read_csv('/home/jethro/文档/pydata-book-master/data/tips.csv')
tips['tip_pct']=tips['tip']/tips['total_bill']
a=pd.pivot_table(tips,index=['smoker','size'])
#print(a)
#只想聚合tip_pct和size,而且想根据day进行分组，将smoker放到列上，day放到行上.
b=tips.pivot_table(['tip_pct','size'],index='day',columns='smoker')
#print(b)
#传入margins=True添加分项小计。
# 这将会添加标签为All的行和列，其值对应于单个等级中所有数据的分组统计，
c=tips.pivot_table(['tip_pct','size'],index='day',columns='smoker',margins=True)
#print(c)
#要使用其他的聚合函数，将其传给aggfunc即可
#例如，使用count或len可以得到有关分组大小的交叉表
d=tips.pivot_table('tip_pct',index='smoker',columns='day',aggfunc=len,margins=True)
#print(d)
#如果存在空的组合（NA），你可能会希望设置一个fill_value
e=tips.pivot_table('size',index=['time','smoker'],columns='day',aggfunc='sum',fill_value=0)
#print(e)
#crosstab的前两个参数可以是数组，Series或数组列表
f=pd.crosstab([tips.time,tips.day],tips.smoker,margins=True)
print(f)
