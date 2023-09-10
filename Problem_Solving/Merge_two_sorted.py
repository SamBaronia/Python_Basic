def Mergetwosorted(arr1, arr2):
	arr = [0 for i in range(len(arr1 + arr2))]
	i = j =k=0
	while i < len (arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arr[k] = arr1[i]
			i += 1

		else :
			arr [k] = arr2[j]
			j += 1
		k += 1
	while i < len (arr1):
		arr[k]= arr1[i]
		i += 1
		k += 1


	while j < len(arr2):
		arr[k] = arr2[j]
		j += 1
		k+=1
	
	return arr

arr1=[1,2,7,4,221]
arr2 = [5,6,7,8,89]

print (Mergetwosorted(arr1, arr2))
