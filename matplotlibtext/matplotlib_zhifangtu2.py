#-*-coding:utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import numpy as np
comp1=np.random.normal(0,1,size=200) #N(0,1)
comp2=np.random.normal(10,2,size=200) #N(10,4)
values=Series(np.concatenate([comp1,comp2]))
values.hist(bins=100,alpha=0.3,color='k',normed=True)
values.plot(kind='kde',style='k--')
plt.show()