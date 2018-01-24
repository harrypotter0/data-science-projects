#!/usr/bin/env python3

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#m = Basemap('mill')
#15.827771, 77.206399
#20.011551, 81.463698
m = Basemap(projection='mill',
            llcrnrlat=8,
            llcrnrlon=68,
            urcrnrlat=38,
            urcrnrlon=98,
            #c=crude,l=low,h=high,f=full
            resolution='l'
)

#m = Basemap(projection='hammer',lon_0=0,resolution='c')

m.drawcoastlines()
m.drawcountries(linewidth=1)
#m.drawstates(color='b')
#m.drawcounties(color='darkred')
#m.fillcontinents()
#m.etopo() #Only works with m=Basemap('mill')
#m.bluemarble() #Only works with m=Basemap('mill')

xs = []
ys = []

Hydlat, Hydlon = 17.385, 78.4867
xpt, ypt = m(Hydlon, Hydlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt, 'c*', markersize=10)

Mumlat, Mumlon = 19.076, 72.8777
xpt, ypt = m(Mumlon, Mumlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt, 'g^', markersize=10)

m.plot(xs, ys, linewidth=3, label='Air distance', color='r')
#m.drawgreatcircle(Mumlon,Mumlat,Hydlon,Hydlat, color='orange', linewidth=3, label='Arc')

plt.legend(loc=4)
plt.title('Basemap Tutorial')
plt.show()
