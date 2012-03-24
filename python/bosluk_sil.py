dizi = raw_input("Bir cumle giriniz:")
# ensar      hamzacebi
i = 0
sonuc = ""
while i <= len(dizi)-1:
	if dizi[i] == " ":
		while dizi[i] == " ":
			i += 1
		sonuc += " "
	else:
		sonuc += dizi[i]
		i += 1
print sonuc
		 
		
