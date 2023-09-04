def reverse(arr, start_ind, end_ind):
	print (arr)
	if start_ind >= end_ind :
		return arr

	arr[start_ind], arr[end_ind] = arr[end_ind], arr[start_ind]
	reverse (arr, start_ind +1, end_ind-1)
	return arr

arr = [1,2,3,4,5,5]
print (reverse(arr, 0, len (arr)-1))