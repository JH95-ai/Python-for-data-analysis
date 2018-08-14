#-*-coding:utf-8-*-
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
def basic_haiti_map(ax=None,lllat=17.25,urlat=20.25,lllon=-75,urlon=-71):
    #创建极球面投影的Basemap实例
    m=Basemap(ax=ax,projection='stere',lon_0=(urlon+lllon)/2,lat_0=(urlat+lllat)/2,llcrnrlat=lllat,urcrnrlat=urlat,lllcrnrlon=lllon,urcrnrlon=urlon,resolution='f')
    #绘制海岸线,州界,国界以及地图边界
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(12,10))
fig.subplots_adjust(hspace=0.05,wspace=0.05)
to_plot=['2a','1','3c','7a']
lllat=17.25;urlat=20.25;lllon=-75;urlon=-71
for code,ax in zip(to_plot,axes.flat):
    m=basic_haiti_map(ax,lllat=lllat,urlat=urlat,lllon=lllon,urlon=urlon)
data=pd.read_csv('/home/jethro/文档/pydata-book-master/data/haiti/Haiti.csv')
cat_data=data[data['category_%s '% code ==1]]
#计算地图的投影坐标
x,y=m(cat_data.LONGITUDE,cat_data.LATITUDE)
m.plot('x,y,k.',alpha=0.5)
ax.set_title('%s:%s ' %(code,english_mapping[code]))

