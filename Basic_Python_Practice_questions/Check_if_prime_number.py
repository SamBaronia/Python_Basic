def isPrime(num):
	for i in range (2, num):
		if num%i == 0:
			print("Note a prime divided by", i)
			break
	else :
		print ("Isprime, divided by None")

isPrime(13)