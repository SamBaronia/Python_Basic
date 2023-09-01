#Swap two variables without using the third variable in Python
def swap (a, b):

	a,b = b ,a

	return a,b


a = int(input())
b = int(input())
print (swap(a,b))