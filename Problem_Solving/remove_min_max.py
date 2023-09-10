def remove_ele(arr):
	while len(arr) > 1:
		arr.remove(min(arr))
		arr.remove(max(arr))
	return arr
arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]

print (remove_ele(arr))
