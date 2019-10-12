#break:
for i in range(10):
	if i == 7:
		print("processing is enough...plz break")
		break
	print(i)
#continue:
for i in range(10):
	if i%2 == 0:
		continue
	print(i)
#pass"
for i in range(10):
	if i == 3:
		pass
	print(i)