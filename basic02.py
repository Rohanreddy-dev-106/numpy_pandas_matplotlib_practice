import numpy as np
import  matplotlib.pyplot as plt
import time as t
#numpy array vs python list speed test

#list
#
# a=[i for i in range(10000000)]
# b=[j for j in range(10000000,20000000)]
# c=[]
# start_time=t.time()
# for i in range(min(len(a),len(b))):
#     c.append(a[i]+b[i])
# print(t.time()-start_time)
#
# print("______________________")
#
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(3,4)
# start_time2=t.time()
# c=a1+a2
# print(c)
# print(t.time()-start_time2)

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

#boolean indexing
bool_index=np.random.randint(1,100,9).reshape(3,3)
print(bool_index[bool_index > 50 ],"kc")
print(bool_index[bool_index%2==0])
print(bool_index[(bool_index%2==0 ) & (bool_index > 30)]) #array[conduction]

#broadcasting
#NumPy automatically stretches smaller arrays to match larger ones (logically, not physically).

a1 = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

#maths formuls
def sigmoid(array): #range from (0,1)
    return 1/(1+ np.exp(-array))

x=np.arange(10)

print(sigmoid(x))
print("________________")
def mse(a,p):
    return np.mean((a-p)**2)
print(mse(x,np.mean(x)),"MSE")

#working with nan

n=np.array([1,2,3,np.nan,4,5,6],dtype=float)
print(n)
l=[]
for i in n:
    if np.isnan(i):
        continue
    l.append(i)
print(l)

print(n[~(np.isnan(n))])# filter with boolen indexing not nan

#ploting graph
#x=y

x=np.linspace(-10,10,100)
y=x
plt.plot(x,y)
plt.show()

#ploting parabola

y2=x**2
plt.plot(x,y2)
plt.show()


