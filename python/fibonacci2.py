n = input("n degerini giriniz:")
i = 1
j = 1
fib = 0
while i <= n:
	j ,fib = fib, j+fib
	i += 1
print float(j) / fib
