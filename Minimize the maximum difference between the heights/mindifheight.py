#Esto es un metodo que hice primero pero no funca bien
def getMinDiff2(arr, k):
	n = len(arr)
	arr.sort()
	maxx, minn = arr[n-1], arr[0]

	if maxx-minn <= k:
		arr = [x+k for x in arr]
		newmax, newmin = arr[n-1], arr[0]
	else:
		arr[0] += k
		arr[n-1] -= k
		newmax, newmin = max(arr[0],arr[n-1]), min(arr[0],arr[n-1])
		for j in range(1,n-1):
			if arr[j]<newmin: arr[j] += k
			elif arr[j]>newmax: arr[j] -= k
			elif (arr[j]-newmin) > (newmax-arr[j]): arr[j] -= k 
			else: arr[j] += k
			newmax, newmin = max(arr[j], newmax), min(arr[j], newmin)

	return(newmax-newmin,arr)

########################
#Esta es la forma cabeza
import itertools
def getMinDiff(arr,k):
	n = len(arr)

	comb = list(itertools.product([k,-k], repeat=n))

	auxlist = [sum(x) for x in zip(comb[0], arr)]
	dif = max(auxlist)-min(auxlist)
	result, resultarr = dif, auxlist
	#resultarr = auxlist

	for i in range(1,2**n):

		auxlist = [sum(x) for x in zip(comb[i],arr)]
		difnew = max(auxlist)-min(auxlist)

		if difnew<dif: 
			result, resultarr = difnew, auxlist
			#resultarr = auxlist
			dif = difnew

	return(result,resultarr)

#Aca pienso todo de cero
def getMinDiffNew(arr,k):
	n = len(arr)

#arr = [1, 2,3]
#k = 2

arr = [51,85,87,120]
k = 20
print(getMinDiff(arr,k))

#Deberia dar 35!
#print(getMinDiff2(arr, k)))

