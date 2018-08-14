#-*-coding:utf-8-*-
import numpy as np
import pandas as pd
tips=pd.read_csv('/home/jethro/文档/pydata-book-master/data/tips.csv')
#添加‘小费占总额百分比’的列
tips['tip_pct']=tips['tip']/tips['total_bill']
def top(df,n=5,column='tip_pct'):
    return df.sort_index(by=column)[-n:]
#根据分组选出最高的5个tip_pct值
a=top(tips,n=6)
print(a)
#对smoker分组并用该函数调用apply
b=tips.groupby('smoker').apply(top)
print(b)
#top函数在DataFrame的各个片段上调用,然后结果由pandas.concat组装在一起，并以分组名称进行了标记.
#于是，最终结果就有了一个层次化索引，其内层索引值来自原DataFrame

#如果传给apply的函数能够接受其他参数或关键字，则可以将这些内容放在函数名后面一并传入
c=tips.groupby(['smoker','day']).apply(top,n=1,column='total_bill')
print(c)
result=tips.groupby('smoker')['tip_pct'].describe()
print(result)
d=result.unstack('smoker')
print(d)
#分组键会跟原始对象的索引共同构成结果对象中的层次化索引.将group_keys=False传入groupby即可禁止
#该效果
e=tips.groupby('smoker',group_keys=False).apply(top)
print(e)

