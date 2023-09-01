def fibonacci_recursive(num):
	if num == 0 or num == 1:
		return 1
	return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

num = 8
for i in range (0, num+1):
	print (fibonacci_recursive (i))