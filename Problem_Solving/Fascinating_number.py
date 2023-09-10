def fascinating(n):
	default = "123456789"
	a , b = n * 2, n * 3

	s = str(n) + str(a) + str(b)
	if sorted(s) == sorted(default):
		return "Fascinating Number"

	return "Not Fascinating"
print (fascinating(193))