computer = int(input())
program = []

while 1 :
	a = input()
	if a == 's':
		print("입력 종료")
		break

	elif a != '\n':
		program.append(int(a))
	print(program)

print(computer)

av = 0

for i in program:
	av = av+i

av = av/computer

print(av)