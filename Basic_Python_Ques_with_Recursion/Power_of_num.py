def power(base, exponent):
	if exponent == 0:
		return 1

	small_Output =  (base*power(base, exponent-1))
	return small_Output

print (power (5, 3))