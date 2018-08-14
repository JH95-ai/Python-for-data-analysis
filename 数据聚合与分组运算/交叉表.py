#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
data=pd.DataFrame({'Sample':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      'Gender':['F', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F'],
      'Handedness':['R', 'L', 'R', 'R', 'L', 'R', 'R', 'L', 'R', 'R']})
#print(data)
a=pd.crosstab(data.Gender,data.Handedness,margins=True)
#print(a)
#crosstab的前两个参数可以是数组，Series或数组列表
