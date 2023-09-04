def replacePi(s):
	if len(s) == 0 or len (s)==1:
		return s

	if s[0]=='p' and s[1] =='i':
		small_Output = replacePi(s[2:])
		return '3.14' + small_Output  

	else :
		small_Output = replacePi (s[1:])
		return s[0] + small_Output 

print (replacePi('ppisamapi'))