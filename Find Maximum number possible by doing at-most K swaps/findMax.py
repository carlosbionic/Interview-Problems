def findMax(lM, k, maxx):
	print(lM)
	if sorted(lM) == list(reversed(lM)) or k == 0: 

		return maxx

	n = len(lM)

	for i in range(n-1):

		for j in range(i+1,n):

			if lM[i]<lM[j]:
				lM[i], lM[j] = lM[j], lM[i]

				if lM > maxx: 

					maxx = lM.copy()

				maxx = findMax(lM, k-1, maxx)

				#Backtrack
				print('BACKTRACK!')
				lM[i], lM[j] = lM[j], lM[i]

	return maxx			


if __name__ == "__main__":
	M = 529
	k = 2
	lM = [int(i) for i in str(M)]
	maxx=lM.copy()

	print(findMax(lM,k,maxx))

