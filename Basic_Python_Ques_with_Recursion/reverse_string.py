def reverse(s):
	if len(s)==0:
		return s

	small_Output =  reverse(s[1:]) + s[0] 
	return small_Output

print (reverse("samarth"))
