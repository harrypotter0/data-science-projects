#!/usr/bin/env/ python3

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [0,0,0,0,0,0,0,0,0,0]

dx = [1,1,1,1,1,1,1,1,1,1]
dy = [1,1,1,1,1,1,1,1,1,1]
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x,y,z,dx,dy,dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
