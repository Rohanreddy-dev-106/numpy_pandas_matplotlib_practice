import numpy as np
import time as t
#numpy array vs python list speed test

#list

a=[i for i in range(10000000)]
b=[j for j in range(10000000,20000000)]
c=[]
start_time=t.time()
for i in range(min(len(a),len(b))):
    c.append(a[i]+b[i])
print(t.time()-start_time)

print("______________________")

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
start_time2=t.time()
c=a1+a2
print(c)
print(t.time()-start_time2)

#Advance indexing

# fancy indexing
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Select rows 0 and 2
print(a[[0, 2]])

#select colomn 0,2
print(a[:,[0,2]])

# Elements at (0,1) and (2,2)
print(a[[0, 2], [1, 2]])


