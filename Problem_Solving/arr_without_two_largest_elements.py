def Two_max(arr):
	if len (arr) < 2:
		return "Enter valid arr"

	max_one = None
	max_two = None

	for i in range (len (arr)):
		curr = arr[i]
		if max_one is None or curr > max_one:
			max_two = max_one
			max_one = curr
		elif max_two is None or curr > max_two and max_two is None or curr == max_two:
			max_two = curr
	
	arr.remove(max_one)
	arr.remove(max_two)
	
	return sorted(arr)

arr = [7, -2, 3, 4, 9, -1]
print (Two_max(arr))

