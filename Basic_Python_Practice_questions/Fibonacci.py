#Fibonacci series program in python using iterative method

def fibonacci(num):
	n1 = 0
	n2 = 1
	if num == 1:
		return 1
	for i in range (num):
		fib = n1+n2
		n1 = n2
		n2 = fib
		print (n2)

(fibonacci(8))