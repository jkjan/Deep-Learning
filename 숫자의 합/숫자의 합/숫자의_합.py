a = int(input())
b = input()
c = 0
for i in range(0, a) :
	c = c + int(b[i:(i+1)])
print(c)