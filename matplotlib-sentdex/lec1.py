import matplotlib.pyplot as plt
from random import randint
x = [randint(0, 9) for i in range(10)]
y = [randint(0, 9) for i in range(10)]

plt.scatter(x,y,label='choo',color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
