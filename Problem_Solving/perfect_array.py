def perfect_arr(arr):
	return "PERFECT" if arr == arr[::-1] else "NOT PERFECT"



arr = [int(i) for i in input("Enter the elements of array separated by space : ").split()]

print (perfect_arr(arr))
