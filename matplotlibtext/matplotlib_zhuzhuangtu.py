#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
from pandas import Series
import numpy as np
fig,axes=plt.subplots(2,1)
data=Series(np.random.randn(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7)
data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)
plt.show()