a = [90, 85, 70]

b = [88, 79, 92]

c = [100, 100, 100]

students = [a, b, c]

for scores in students :
	print(scores)


for scores in students :
	total = 0
	for s in scores :
		total = total+s
	average = total/3
	print(scores, total, average)