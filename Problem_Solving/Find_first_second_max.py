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
		elif curr > max_two and curr == max_two:
			max_two = curr
	
	
	return (max_one, max_two)

arr = [2,4,1,23,31,2,313,23,1424,1424,1]
print (Two_max(arr))

