def palindrome(s, l, h):
	if l >= h :
		return True

	if s[l] != s[h]:
		return False
	return palindrome(s, l+1, h - 1)

s = "carac"
print(palindrome(s, 0, len(s)-1))
