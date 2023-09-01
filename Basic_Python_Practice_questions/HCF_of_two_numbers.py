def hcf (a, b):
	min_num = min(a, b)
	for i in range (1, min_num+ 1):
		if (a % i == 0) and (b % i == 0):
			HCF = i
	return HCF

print (hcf (100, 4060))
