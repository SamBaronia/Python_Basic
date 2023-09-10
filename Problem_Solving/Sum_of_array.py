def sums (arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]
print (sums(arr))