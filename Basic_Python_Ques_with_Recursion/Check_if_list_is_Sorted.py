def isSorted(a):
	l = len (a)
	if l ==0 or l == 1:
		return True
	for i in range (0, l-1):
		if a[i] > a[i+1]:
			return False
			break
	return True

a = [1,2,3,4,5,22,43,64,75,566,4666]
print(isSorted(a))

