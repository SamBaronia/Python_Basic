def fact(n):
	fac = 1
	while n > 0:
		fac = fac * n
		n-= 1
	return fac

print(fact(6))