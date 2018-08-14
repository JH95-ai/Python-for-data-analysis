#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import cm
from matplotlib import rcParams
from matplotlib.collections import LineCollection
from pandas import DataFrame, Series
fec=pd.read_csv('/home/jethro/文档/pydata-book-master/data/fec/P00000001-ALL.csv')
#print(fec)
#print(fec.ix[123456])//随便抽取一条记录
#该数据没有党派信息,因此最好把它加进去。通过unique,可以获取全部的候选人名单
a=unique_cands=fec.cand_nm.unique()#候选人去重
#print(a[2])
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
              'Gingrich, Newt': 'Republican',
               'Huntsman, Jon': 'Republican',
               'Johnson, Gary Earl': 'Republican',
               'McCotter, Thaddeus G': 'Republican',
               'Obama, Barack': 'Democrat',
              'Paul, Ron': 'Republican',
               'Pawlenty, Timothy': 'Republican',
               'Perry, Rick': 'Republican',
              "Roemer, Charles E. 'Buddy' III": 'Republican',
               'Romney, Mitt': 'Republican',
               'Santorum, Rick': 'Republican'} # 构造党派对应信息"
#现在通过这个映射以及Series对象的map方法，你可以根据候选人姓名得到一组党派信息
b=fec.cand_nm[123456:123461]
#print(b)
c=fec.cand_nm[123456:123461].map(parties)
#print(c)
fec['party'] = fec.cand_nm.map(parties)  # 添加新列
d=fec['party'].value_counts()  #统计各个党派的数量
#print(d)
e=(fec.contb_receipt_amt > 0).value_counts() # 出资状况统计，False表示钱又要回去的。
#print(e)
fec = fec[fec.contb_receipt_amt > 0] # 根据出资条件筛选
# 再精简一下范围，只包括奥黑和罗姆尼
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
# 根据职业和雇主统计赞助信息
f=fec.contbr_occupation.value_counts()[:10]
# 退休人士如此给力？
#print(f)
occ_mapping = {'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
               'INFORMATION REQUESTED': 'NOT PROVIDED',
               'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',
              'C.E.O.': 'CEO'}
# 职业映射，便于做合并。
f = lambda x: occ_mapping.get(x, x)
# get的两个参数，第一个是key，第二个是找不key到返回的默认值。
fec.contbr_occupation = fec.contbr_occupation.map(f)

emp_mapping = {'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
                   'INFORMATION REQUESTED': 'NOT PROVIDED',
                   'SELF': 'SELF-EMPLOYED',
                   'SELF EMPLOYED': 'SELF-EMPLOYED'}
#处理雇主信息
f= lambda x: emp_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)
#通过pivot_table根据党派和职业对数据进行聚合,然后过滤掉总出资额不足200万美元的数据
# 根据捐款总额生成透视表
by_occupation = fec.pivot_table('contb_receipt_amt',
                                    index='contbr_occupation',
                                   columns='party',
                                   aggfunc='sum')

over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
# 超过2M的狗大户，sum(1)代表沿着行的方向相加。
#print(over_2mm)
#将这些数据做成柱状图
over_2mm.plot(kind='barh')
#plt.show()
#总出资额最高的职业和企业，先对候选人进行分组，然后使用求取最大值的方法.
def get_top_amounts(group, key, n=5):
# 分组后找key的topX条记录
        totals = group.groupby(key)['contb_receipt_amt'].sum()
        #根据key对totals进行降序排列
        return totals.sort_values(ascending=False)[:n]
# 原来的代码[n:]不对
#根据职业和雇主进行聚合
# 根据职业
grouped = fec_mrbo.groupby('cand_nm')
a=grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
#print(a)
#根据雇主
b=grouped.apply(get_top_amounts,'contbr_employer',n=10)
#print(b)
#利用cut函数根据出资额的大小将数据离散化到多个面元中
bins=np.array([0,1,10,100,1000,10000, 100000, 1000000, 10000000])
#根据捐款额划分区间
labels=pd.cut(fec_mrbo.contb_receipt_amt,bins)
#print(labels)
#根据候选人姓名以及面元标签对数据进行分组
grouped=fec_mrbo.groupby(['cand_nm',labels])
d=grouped.size().unstack(0)#把外行索引变成列
#print(d)
#对出资额求和并在面元内规格化，以便图形化显示两位候选人各种赞助额度的比例
bucket_sums=grouped.contb_receipt_amt.sum().unstack(0)#金额汇总
#print(bucket_sums)
#对每一行进行归一化
normed_sums=bucket_sums.div(bucket_sums.sum(axis=1),axis=0)
#print(normed_sums)
#去掉最后两行，以堆叠柱状图展现
normed_sums[:-2].plot(kind='barh',stacked=True)
#plt.show()
#根据候选人和州对数据进行聚合
grouped=fec_mrbo.groupby(['cand_nm','contbr_st'])#根据候选人和州分组
totals=grouped.contb_receipt_amt.sum().unstack(0).fillna(0)#各州收到的金额汇总
totals=totals[totals.sum(1)>100000]#金额大于十万的州
#print(totals[:10])
#各州对候选人的捐助比例
percent=totals.div(totals.sum(1),axis=0)
print(percent[:10])

