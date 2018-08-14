import matplotlib.pyplot as plt
from numpy.random import randn
data=randn(30).cumsum()
plt.plot(data,'k--',label='Default')
plt.plot(data,'k--',drawstyle='steps-post',label='steps-post')
plt.legend(loc='best')
#plt.plot(randn(30).cumsum(),color='k',linestyle='dashed',marker='o')
plt.show()