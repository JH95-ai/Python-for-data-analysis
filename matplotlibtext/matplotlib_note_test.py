#-*-coding:utf-8-*-
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame,Series
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
data=pd.read_csv('/home/jethro/文档/pydata-book-master/data/spx.csv')
spx=data['SPX']
spx.plot(ax=ax,style='k-')
crisis_data={(datetime(2007,10,11),'Peak of bull market'),
             (datetime(2008,3,12),'Bear Stearns Fails'),
             (datetime(2008,9,15),'Lehman Bankrupty')}
for date,label in crisis_data:
    ax.annotate(label,xy=(date,spx.asof(date)+50),xytext=(date,spx.asof(date)+200),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',verticalalignment='top')
#放大到2007-2010
ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,1800])
ax.set_title('Important dates in 2008-2009 financial crisis')
# 第一个参数是注释的内容
# xy设置箭头尖的坐标
# xytext设置注释内容显示的起始位置
# arrowprops 用来设置箭头
# facecolor 设置箭头的颜色
# headlength 箭头的头的长度
# headwidth 箭头的宽度
# width 箭身的宽度
plt.show()