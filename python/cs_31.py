n = input("Bir sayi giriniz:")
i = 1
fib = 0
j =1
while j <= n:
	i, fib = fib, i+fib
	j += 1
	print fib,

