def binary(num):
	
	while num>0:
		if num%10 != 0 and num%10 != 1:
			return False

			break
		num = num//10
		if num ==0:
			return True

print (binary(11001))