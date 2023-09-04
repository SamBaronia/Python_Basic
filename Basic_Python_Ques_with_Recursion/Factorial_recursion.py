def fact(n):
	print("starts for", n)
	if n == 0:
		
		return 1

	print("end for", n)
	return n * fact(n-1)

print (fact(5))