a = int(input())
for i in range(1,a+1):
	if i == a:
		print('*'*a)
		break
	print(' '*(a-i-1),'*'*i)