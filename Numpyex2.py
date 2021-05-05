import numpy as np

arr = np.array([[1, 5, 6],
               [4, 7, 2],
               [3, 1, 9]])

print('Largest element is: ', arr.max())
print('Row-wise maximum element: ', arr.max(axis = 1))
print('Column wise minimum element: ', arr.min(axis = 0))
print('Sum of all array element: ',arr.sum())
print('Cumulative sum along each row: \n', arr.cumsum(axis = 1))
