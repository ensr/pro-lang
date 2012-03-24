v = input("Lutfen vize notunu giriniz:")
f = input("Lutfen final notunu giriniz:")
ort = (v*40 + f*60) / 100

if ort < 60:
	print "Ortalamaniz:", ort, "Kaldiniz."
else:
	print "Ortalamaniz:", ort, "Gectiniz."	
