#Python program for palindrome using an iterative method

def palindrome(num):
	original_num = num 
	potential_palindrome = 0
	
	while num>0:
		potential_palindrome = (potential_palindrome*10) + (num%10)
		num = num//10

	if potential_palindrome == original_num:
		return True, potential_palindrome

	return False, potential_palindrome

print (palindrome(1212))

