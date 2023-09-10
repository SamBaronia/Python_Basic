def equal_ind(arr):
	return [arr[i] for i in range (0, len(arr), 2) if arr[i] == i]



arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]

print (equal_ind(arr))
