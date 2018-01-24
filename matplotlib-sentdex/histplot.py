#!/usr/bin/env python3

import matplotlib.pyplot as plt

population_ages = [19,33,110,48,53,12,6,19,88,44,43,32,26,22,20,65,78,72,33]
ids = [x for x in range(len(population_ages))]
bins = [x * 10 for x in range(13)]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
#plt.hist(population_ages, bins, rwidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\n')
plt.show()
