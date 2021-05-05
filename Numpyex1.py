import numpy as np

a = np.array([1, 2, 3, 5])

print('Adding 1 to every Element: ', a+1)

print('Subtracting 3 from each element: ', a-3)

print('Multiplying each element by 10: ', a*10)

print('Squaring each Element: ', a**2)

print('Double each element of original Array: ', a)


a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print('\n Original Array: \n', a)
print('Transpose of Array: \n',a.T )