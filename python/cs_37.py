def tersten_yazdirma(string):
	for i in range(len(string)*2):
		if i < len(string):
			print string[len(string)-1-i]
		else:
			print string[i%len(string)]
input()
