#Program to Find the max of n numbers in python

n = (input())
arr = [int(x) for x in (n.split())]

print (arr)

max_num = None

for i in range(len(arr)):
	if max_num is None or arr[i] > max_num:
		max_num = arr[i]

print (max_num) 