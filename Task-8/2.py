import numpy as np


a=int(input("Enter Size of first array:"))
m=[]
for i in range(a):
    i=int(input("Element: "))
    m.append(i)
b=np.array(m)
print(b)

a1=int(input("Enter Size of second array:"))
m1=[]
for i in range(a1):
    i=int(input("Element: "))
    m1.append(i)
b1=np.array(m1)
print(b1)

comparison = b == b1
equal_arrays = comparison.all()

print(equal_arrays)

