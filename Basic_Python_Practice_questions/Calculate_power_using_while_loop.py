def power (a, b):

	res = 1
	while b > 0:
		res = res * a
		b -= 1
	return res

a = int (input ("Enter Base : "))
b = int (input ("Enter Power : "))
print (power(a, b))