#-*-coding:utf-8-*-
from pandas import DataFrame,Series
import numpy as np
import pandas as pd
columns=pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],[1,3,5,1,3]],names=['cty','tenor'])
hier_df=DataFrame(np.random.randn(4,5),columns=columns)
print(hier_df.groupby(level='cty',axis=1).count())
