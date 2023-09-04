def Binarysearch(arr, x, si, ei):
	if si > ei :
		return -1

	mid = (ei + si) //2
	if arr[mid] == x:
		return mid 

	if arr[mid]> x:
		return Binarysearch(arr, x, si , mid -1 )

	else :
		return Binarysearch (arr, x, mid + 1, ei)

arr = [1,2,3,4,4,5,6,6,6,653,4455,6645,43223]
print (Binarysearch(arr, 6, 0, len(arr)-1))