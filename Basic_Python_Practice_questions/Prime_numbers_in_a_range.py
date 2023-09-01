def prime (a, b):
	if a == 1 and b == 2:
		return print (2)

	for i in range (a, (b+1)//2):
		if i == 1:
			continue

		flag = 1

		for j in range (2, i//2 +1):
			if (i % j == 0):
				flag = 0
				break
				

		if flag == 1:
			print (i, end = " ")

a = int (input("enter the lower bound :"))
b = int (input("enter the upper bound :"))
prime(a, b)