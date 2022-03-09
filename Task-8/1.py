import numpy as np

list1 = [10, 11, 12, 13, 14]
vector1 = np.array(list1)
p = 5
new = np.zeros(len(vector1) + (len(vector1)-1)*(p))
new[::p+1] = vector1
print("Horizontal Vector")

print(vector1)



print("\nNew vector:")
print(new)




