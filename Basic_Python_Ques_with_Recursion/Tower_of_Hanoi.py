def TowerOfhanoi(n, a,b,c):
	if n ==1 :
		print ("move disk from", a, "to", c)
		return

	TowerOfhanoi(n-1, a, c, b)
	print ("moving", n, "th disk from", a, c)
	TowerOfhanoi (n-1, b,a,c)

TowerOfhanoi(3, "First Rod", "Helper rod", "Destination rod")