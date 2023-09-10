def remove_ele(arr):
	mid = len (arr)//2
	arr1 = arr[:mid]
	arr2 = arr[mid:]

	if sum(arr1) == sum(arr2):
		return "Already balanced"
	elif sum(arr1) > sum (arr2):
		return sum(arr1) - sum(arr2)
	else :
		return sum(arr2) - sum(arr1)

arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]

print (remove_ele(arr))
