def down_pyramid(n):
	m = (n *2) -2
	for i in range (0, n + 1):
		for j in range (1, m):
			print (end = " ")
		m -= 1

		for k in range (i + 1):
			print ("*", end = " ")
		print ()

down_pyramid (5)