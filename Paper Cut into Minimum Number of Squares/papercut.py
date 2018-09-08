def cutRect(a,b):

	# Save the minimum in b
	if a < b: a, b = b, a 

	if a%b == 0:
		return int(a/b)

	result = 0
	rem = 0

	while(b > 0):
		result += int(a/b)
		rem = int(a%b)

		a = b
		b = rem
	return result

def rectCarlos(a,b):

	# Save the maximum in a
	if a < b: a, b = b, a
	
	result = 0

	while b > 0:

		result += int(a/b)
		large = a
		a = b
		b = (large%b)
	
	return result
	

print(cutRect(13,11))
print(rectCarlos(13,11))
