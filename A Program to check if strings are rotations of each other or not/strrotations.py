def isRotations (s1,s2):

	l1 = list(s1)
	l2 = list(s2)
	aux = list(l2)
	print(l1,l2)


	if len(l1) != len(l2):
		return False

	else:
		for i in range(-len(l1),0):
			for j in range(i,i+len(l1)):
				aux[j-i] = l2[j]
			if l1 == aux:
				return True
		else:
			return False

def isRotations2 (s1,s2):

	if len(s1) != len(s2):
		return False

	conc = s1 + s1
	for i in range(len(s1)):
		if s2 == conc[i:i+len(s1)]:
			return True
	else:
		return False

print(isRotations2('abcd','dasbc'))
