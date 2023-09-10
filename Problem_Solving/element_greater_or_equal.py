def element(arr, x):
	count = 0
	for i in arr:
		if i <= x:
			count += 1
	return count 

arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]
x = int (input("Enter the element to be compared with : "))

print (element(arr, x))

