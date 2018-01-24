#!/usr/bin/env python3

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,8]

plt.plot(x,y, label='First Line')
plt.plot(x2,y2, label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important Variable')
plt.title('Interesting Graph\n')
plt.legend()
plt.show()
