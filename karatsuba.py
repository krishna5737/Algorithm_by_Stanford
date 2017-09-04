

def karatsuba(x,y):
	lx = len(str(x))
	ly = len(str(y))
	if(lx == 1 or ly == 1):
		return(x*y)
	else:
		if (lx>ly):
			n = lx
		n = ly
		floor = int(math.floor(n+(n % 2)/2)) - (n % 2)
		ceil = int(math.ceil(n+(n % 2)/2)) - (n % 2)
		a = str(x)[0:floor]
		b = str(x)[ceil:n]
		c = str(y)[0:floor]
		d = str(y)[ceil:n]
		
		part1 = (10**n)*karatsuba(a,c)
		part2 = karatsuba(b,d)
		partt3 = (karatsuba((a+b),(c+d)) - part1-part2)
		product = part1 + part2 + (10**n//2)*part3
		return(product)
print(karatsuba(4,5087))
