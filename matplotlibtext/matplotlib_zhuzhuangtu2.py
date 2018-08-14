#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=DataFrame(np.random.rand(6,4),
             index=['one','two','three','four','five','six'],
             columns=pd.Index(['A','B','C','D'],name='Genus'))
df.plot(kind='barh',stacked=True,alpha=0.5)
#s.value_counts().plot(kind='bar')
plt.show()
