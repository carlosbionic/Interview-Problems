def power(x, y):
	
	res = 1
	for i in range(y):
		res = res*x

	return res

def modexp (x, y, p):
	
	res = 1
	for i in range(y):
		res = res*x

	return res%p

def modexp2 (x, y, p):
	return ((x%p)**y)%p

def modexp3 (x, y, p):

	res = 1
	x = x%p

	for i in range(y):
		res = res*x

	res = res%p

	return res


x=531
y=19
p=6

result = modexp(x,y,p)
result2 = modexp2(x,y,p)
result3 = modexp3(x,y,p)

print(result,result2,result3)
