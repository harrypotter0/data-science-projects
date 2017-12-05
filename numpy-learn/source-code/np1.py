
import numpy as np

L = list(range(10))
print(L)
print(type(L[0]))

L2= list(str(c) for c in L)
print(L2)
print(type(L2[0]))
L3= [True,"2",3.0,4]
print([type(i) for i in L3])
