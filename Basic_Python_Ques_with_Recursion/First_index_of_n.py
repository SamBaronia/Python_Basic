def indexN(arr, x) :
	si = 0
	l = len (arr)
	if l == 0:
		return -1  
	for i in range (0, l):
		if arr[si] == x:
			return si + 1
		si += 1
	return -1

print (indexN([1,2,3,4,5,5,6,6,7,8,8], 8))