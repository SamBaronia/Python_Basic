def power (a, b):

	res = 1
	for i in range (0, b):
		res = res * a
	return res

a = int (input ("Enter Base : "))
b = int (input ("Enter Power : "))
print (power(a, b))