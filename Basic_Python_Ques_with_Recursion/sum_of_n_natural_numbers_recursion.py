def sums (n):
	if n == 0 :
		return 0
	elif n == 1:
		return 1

	return (n + sums (n-1 ))

print (sums (10))  