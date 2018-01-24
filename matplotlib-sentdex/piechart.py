#!/usr/bin/env python3

import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
cols = ['c', 'm', 'r', 'g']
plt.pie(slices, 
        labels=activities, 
        colors=cols, 
        startangle=135, 
        shadow=True, 
        explode=(0,0.1,0,0), 
        autopct='%1.1f%%')
plt.title('Interesting Graph\n')
plt.show()
