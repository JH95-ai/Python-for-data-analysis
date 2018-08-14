import matplotlib.pyplot as plt
from numpy.random import randn
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum())
ticks=ax.set_xticks([0,250,500,750,1000])
labels=ax.set_xticklabels(['one','two','three','four','five'])
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
plt.show()
