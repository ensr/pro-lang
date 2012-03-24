def pat(s,p):
	for i in range(len(s)):
		if s[i:i+len(p)] == p:
			return True
	return False 
print hop("1110110010110110010","1010")
