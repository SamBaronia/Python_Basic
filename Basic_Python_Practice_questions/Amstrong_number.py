# It is a number which is equal to the sum of cube of its digits.
# For eg: 153, 370 etc.

def Amstrong_number(num):
	ams = 0
	original_num = num
	while num >0 :
		digit = num % 10
		ams = ams + digit**3
		num = num //10


	if ams == original_num:
		print (ams)
		return True
	return False


print (Amstrong_number(370))