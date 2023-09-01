s = "absdajb123412!@@#$"
alp =[]
num = []
spe =[]
for i in s:
	if ord(i)>= 33 and ord(i) <= 47:
		spe.append(i)

	elif ord(i)>= 48 and ord(i)<=57:
		num.append(int(i))

	elif ord(i )> 64 and ord(i)<=90:
		alp.append(i)

	elif ord(i) >= 97 and ord(i)<= 122:
		alp.append(i)

	else:
		spe.append(i)

	

print(alp, num, spe)