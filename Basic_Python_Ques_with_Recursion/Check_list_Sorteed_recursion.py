def isSorted(arr, si) :
	l = len (arr)
	if si == l-1 or si == l :
		return True
	if arr[si] > arr[si+1]:
		return False
	recur = isSorted(arr, si+1)
	return recur

print (isSorted([1,2,3,4,5,5,6,6,7,8,8], 0))