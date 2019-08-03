import numpy as np

#do not use rank 1 array (1행짜리 행렬을 생성하지 말것(row vector)

a = np.random.randn(5,1) #5행 1열 행렬을 랜덤으로 생성
print(a)
print(a.T)
print(np.dot(a.T, a))

#a = a.reshape((5,1))