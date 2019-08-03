import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
                 [1.2, 104.0, 52.0, 8.0],
                 [1.8, 135.0, 99.0, 0.9]])

#print(A)

cal = A.sum(axis = 1, keepdims = True)   #axis = 0 : 세로로 더함 axis = 1 : 가로로 더함

print(cal)

#percentage = 100*A/cal.reshape(1,4)

#print(percentage)