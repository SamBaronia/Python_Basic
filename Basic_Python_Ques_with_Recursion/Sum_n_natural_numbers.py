def sums (n):
	if n == 1:
		return 1
	sumss = 0
	for i in range (n+1):
		sumss += i
	return sumss


print (sums (100))