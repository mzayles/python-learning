import numpy as np

arr = np.arange(1, 11, dtype=int)
print(arr)

# indexação de unidimensionais
print(arr[4])                                        
print(arr[2:5])
print(arr[:5])
print(arr[2:])

# indexação de bidimensionais
arr2 = np.random.randint(10, 50, size=[3,3])
print(arr2)

print(arr2[1][1])
print(arr2[1][2])
print(arr2[2][0:2])

arr3 = np.random.randint(1, 101, size=[10, 10])
print(arr3)

print(arr3[3][3])
print(arr3[0:3, 7:])
print(arr3[2:4, 6:9])