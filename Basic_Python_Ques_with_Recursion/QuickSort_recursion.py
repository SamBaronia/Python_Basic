def QuickSort(arr):
	if len (arr) <= 1:
		return arr
	pivot = arr.pop()
	small =[]
	large =[]
	i =0
	while i < len(arr):
		if arr[i] > pivot:
			large.append(arr[i])
		else: 
			small.append(arr[i])
		i += 1

	return QuickSort(small) + [pivot] + QuickSort(large)

arr = [22,3,45,32,1,2,3,5,7,76,5,3,1]
print (QuickSort (arr), len (arr))