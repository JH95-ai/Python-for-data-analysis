#-*-coding:utf-8-*-
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
df=DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
df.plot()
plt.show()
