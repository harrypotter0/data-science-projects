import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [2,4,5,5,5]

y2 = [2,4,6,8,10]
x2 = [2,4,5,5,5]


plt.bar(x,y,label='Bars1')
plt.bar(x2,y2,label='Bars2')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
