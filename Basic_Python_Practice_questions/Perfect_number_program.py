def perfect_num(num):
	test_sum = 0

	for i in range (1,(num//2)+ 1):
		if num %i == 0:
			test_sum += i

	if test_sum == num :
		return True
	return False


print (perfect_num(6))