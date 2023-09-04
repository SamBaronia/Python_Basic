def indexN(arr, x, si) :
	l = len (arr)
	if si == l:
		return -1  
	if arr[si] == x:
		return si
	
	recur = indexN(arr, x, si + 1)
	return recur

print (indexN([1,2,3,4,5,5,6,6,7,8,8], 9, 0))