#python-program-to-reverse-a-number

def reverse_integer(num):
	reverse = 0
	while num > 0 :
		remainder = num%10
		reverse = reverse*10 + remainder
		num = num//10
	return reverse

print (reverse_integer(1236216873612))
