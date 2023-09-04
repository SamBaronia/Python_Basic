
def palin (num, rev):
	if num == 0 :
		return rev
	rev = (rev * 10) + (num %10)
	return palin(num//10, rev)

num = 101
rev = palin (101, 0)
