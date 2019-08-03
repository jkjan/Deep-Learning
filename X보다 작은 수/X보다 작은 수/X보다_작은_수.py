N, X = input().split()
N = int(N)
X = int(X)
L = list(map(int, input().split()))

for i in range (0, N):
	if L[i] < X:
		print(L[i], end=' ')