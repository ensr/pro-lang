def pat_say(s,p):
	sayac = 0
	for i in range(len(s)):
		if s[i:i+len(p)] == p:
			sayac += 1
	print sayac
pat_say("1010111010111010","10")
