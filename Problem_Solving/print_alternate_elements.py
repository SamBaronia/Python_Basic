def alternate_element(arr):
	return [arr[i] for i in range (0, len(arr), 2)]



arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]

print (alternate_element(arr))
