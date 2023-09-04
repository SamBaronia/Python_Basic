def lastindexN(arr, x, si) :
	l = len (arr)
	if si == 0 :
		return -1  
	if arr[si] == x:
		return si
	
	recur = lastindexN(arr, x, si -1)
	return recur
arr = [i for i in range (1, 1000, 1)]
print (lastindexN(arr,999, len (arr)-1))