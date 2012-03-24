dizi = raw_input("Bir cumle giriniz:")
liste = dizi.split(" ")
en_uzun = []
uzunluk = []
for i in liste:
	uzunluk.append(len(i))
en_uzun = uzunluk.index(max(uzunluk))
print liste[en_uzun]
			 
	
