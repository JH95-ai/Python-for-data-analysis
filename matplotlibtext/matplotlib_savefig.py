#-*-coding:utf-8-*-
from io import StringIO
import matplotlib.pyplot as plt
buffer=StringIO
plt.savefig('figpath.svg')
plt.savefig('figpath.png',dpi=400,bbox_inches='tight')
plt.savefig(buffer)
plot_data=buffer.getvalue()
plt.rc('figure',figsize=(10,10))
font_options={'family':'monospace',
              'weight':'bold',
              'size':'small'}
plt.rc('font',**font_options)