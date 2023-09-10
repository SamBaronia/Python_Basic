def Mergetwosorted(arr1, arr2):
	arr = []
	i = j =0
	while i < len (arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arr += [arr1[i]]
			i += 1

		else :
			arr += [arr2[j]]
			j += 1

	while i < len (arr1):
		arr += [arr1[i]]
		i += 1


	while j < len(arr2):
		arr += [arr2[j]]
		j += 1
	
	return arr

arr1=[1,2,3,5,6]
arr2 = [0,6,6,6,7,8]

print (Mergetwosorted(arr1, arr2))
