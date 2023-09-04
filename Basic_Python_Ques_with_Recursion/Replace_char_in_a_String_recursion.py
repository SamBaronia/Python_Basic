def replaceChar (s, a,b):
	if len (s) == 0:
		return s

	small_Output = replaceChar (s[1:], a, b)

	if s[0] == a:
		return b + small_Output

	else:
		return s[0] + small_Output

print (replaceChar('Samarth', 'a', 'x'))