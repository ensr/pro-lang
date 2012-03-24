def pat(s,p):
	for i in range(len(s)):
		if s[i:i+len(p)] == p:
			return True
	return False 
print pat("1110110010110110010","1010")
