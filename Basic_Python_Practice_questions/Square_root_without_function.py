def SQRT(num ):
	x = num
	y = 1.00000
	z = 0.00001
	while x-y > z:
		x = (x+y) /2
		y = num/x

	return x

num = int (input ("Enter the number : "))
print (abs(SQRT (num)))