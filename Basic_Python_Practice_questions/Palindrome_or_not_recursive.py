#Palindrome program in Python using recursive method
potential_palindrome = 0
def palindrome (num):
	global potential_palindrome
	original_num = num
	if num >0:
		potential_palindrome = (potential_palindrome*10) + (num %10)
		palindrome (num//10)

	if potential_palindrome == original_num:
		return True, potential_palindrome

	return False, potential_palindrome

print (palindrome (1221))