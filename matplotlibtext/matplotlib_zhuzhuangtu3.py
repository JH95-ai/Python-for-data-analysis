#-*-coding:utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import csv
tips=pd.read_csv('/home/jethro/文档/pydata-book-master/data/tips.csv')
party_counts=pd.crosstab(tips.day,tips.time)
party_pcts=party_counts.div(party_counts.sum(1).astype(float),axis=0)
#print(party_pcts)
party_pcts.plot(kind='bar',stacked=True)
plt.show()
