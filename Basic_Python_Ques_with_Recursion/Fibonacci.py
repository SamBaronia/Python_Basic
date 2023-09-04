def fibi (n):
	n1 = 0
	n2 = 1
	for i in range (n-1):
		fib = n1 + n2
		n1 = n2
		n2 = fib
		print (n2)

	return fib

print (fibi(9))