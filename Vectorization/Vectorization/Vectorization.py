import numpy as np

a = np.array([1,2,3,4])

print (a)

import time
a = np.random.rand(1000000)

b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)  #numpy 에서 두 벡터의 내적 A(transposed) * B
toc = time.time()

print(c)
print("Vectorized version :" + str(1000*(toc-tic)) + "ms")

#non-vectorized version


c = 0
tic = time.time() #타임 스탬프

for i in range (1000000) :
    c += a[i]*b[i]
toc = time.time()

print(c)
print("for loop :" + str(1000*(toc-tic)) + "ms")

#벡터로 계산하면 3~400배 빠름