kelime = raw_input("Bir kelime giriniz:")
sesli = "aeiouAEIOU"
sessiz = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
rakam = "1234567890"
sl = 0
ss = 0
sm = 0
rk = 0
for i in kelime:
	if i in sesli:
		sl += 1
	elif i in sessiz:
		ss += 1
	elif i in rakam:
		rk += 1
	else:
		sm += 1
print "sesli:",sl,"\nsessiz:",ss,"\nrakam:",rk,"\nsimge:",sm
