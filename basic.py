import  numpy as np
#in NumPy, arrays are homogeneous If you mix types, NumPy converts everything to a single common type

#1D Array
a=np.array([1,2,3])
print(a)
print("---------------")
#2d Array
b=np.array([[1,2,3],[4,5,6]])
print(b)
print("---------------")
# 3d Array
c=np.array([[[1,2,3],[4,5,6]]])
print(c)
# dtype
c=np.array([1.2,2.1,3.4],dtype=float)
print(c)
print("---------------")
#arange is for creating array  and reshap is for creating matrix note  matrix(row*colomn = range)
z=np.arange(1,13,dtype=int).reshape(3,4)
print(z)
for i in z:
    print(i)
print("---------------")
# we can create  all once matrix
for i in np.ones((3,4),dtype=int):
    print(i)
print("---------------")
# we can create  all zero matrix
for i in np.zeros((3,4)):
    print(i)
print("---------------")
R=np.round(np.random.random((3,4))*100)
for i in np.astype(R,int):
    print(i)

print("---------------")
#It creates 10 evenly spaced numbers from -10 to 10.
for i in np.linspace(-10,10,10):
    print(i)

# a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a3.ndim)
print(a3.shape)
print(a3.size)
print(a3.itemsize)

#scalar operations on arrays

a1=np.arange(1,13,dtype=float).reshape(3,4) #Scalar
print(2 * a1)
print("______________")
print(2 / a1)
print("______________")
print(2- a1)
print("______________")
print(2 + a1)
print("______________")
print(a1**2)
print(a1)
print(a1 >=5)
print("______________")
#vector operations like  array + array or matrix +matrix 1d,2d,3d any hear each returns a new array
a = np.array([1, 2, 3,4]).reshape(2,2)
b = np.array([4, 5, 6,7]).reshape(2,2)
print(a + b)
print(a - b)
print(b / a)
print(b * a)
print("______________")
#min max sum prod
a=np.random.random((1,12))*100
r=np.round(a)
final_result= r.astype(int).reshape(3,4)
print(final_result)

sum=np.sum(final_result)
print(sum)

max=np.max(final_result)
print(max)

min=np.min(final_result)
print(min)
product=np.prod(final_result)
print(product)
print("______________")
#mean/median/std/var
print(np.mean(final_result, axis=1)) #axise=1 for row rows 0 for coloums
print(np.median(final_result, axis=1))
print(np.std(final_result, axis=1))
print(np.var(final_result, axis=1))

print("______________")
#Dot product or two matrixs
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])   # Shape: (2, 3)

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])   # Shape: (3, 2)

C = np.dot(A, B)
print(C)

#Access and slicing

a = np.array([10, 20, 30, 40, 50])
b = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])
c = np.array([
    [
        [1,  2,  3],
        [4,  5,  6]
    ],
    [
        [7,  8,  9],
        [10, 11, 12]
    ]
])
print(a[-2])#normal list indexing  positive and negative

print(b[0,1]) #[row,coloum]

print(c[0,1,2])#[which array ,row,coloum]

print(a[:: 2])
print(a[3:0:-1])
print(a[-1:-4:-1])

print(b[0:2,1:3])#[startrow:endrow , startcolum:endcolum]

print(c[0:2,0:3,0:2]) #c[ depthstart:depthend , startrow:endrow,  startcolum:endcolum]

print("----------")
#update by indix,slicing
#NumPy updates are in-place
#Slicing returns a view, not a copy mean if we change in sliced array it effect orginal array  they  both share same memory
x = np.array([10, 20, 30, 40, 50])
x[2] = 99
print(a)
x[1:4] = 0
print(x)
y = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
])
y[1, 2] = 99
print(y)
print("----------")
#looping in  numpy arrays
for i in b:
    if np.array_equal(i,[5,6,7,8]):#it internally changes to np array  norma list
        continue
    print(i)
for i in np.nditer(b):
    print(i)
print("----------")

#transpose ,ravel flattens an n-D array into a 1-D array
c=np.transpose(b)
print(c)
c=np.ravel(b)
print(c)
print("----------")
# horizontal stacking
a4 = np.arange(12,dtype=int).reshape(3,4)
a5 = np.arange(12,24,dtype=int).reshape(3,4)
print(np.hstack((a4,a5)))
print()
print(np.vstack((a4,a5)))