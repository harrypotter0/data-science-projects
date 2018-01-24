import matplotlib.pyplot as plt

slices = [2,45,52,5,4]

people = ['akash','kanika','malti','mahesh','meenu']
cols = ['c','m','r','b','k']

plt.pie(slices,
        labels=people,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0,0,0,0.1),
        autopct='%.2f'
)

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
#plt.legend()
plt.show()
