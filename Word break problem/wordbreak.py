import numpy as np

def wordBreak(dic, inp):

	n = len(inp)

	if n == 0:
		return True

	for i in range(n):
		if inp[0:i+1] in dic and wordBreak(dic, inp[i+1:n]):
			return True

	else:
		return False

def wordBreakDP(dic, inp):

	n = len(inp)

	if n == 0:
		return True

	dp = np.zeros(n, dtype=bool)

	for i in range(n):

		if inp[0:i+1] in dic:
			dp[i] = True

		else:
			
			for j in range(0,i):

				if dp[j] == True and inp[j+1:i+1] in dic:
					dp[i] = True
					break

	return dp[n-1]

def wordBreakBackT(dic, inp, result):
	
	n = len(inp)

	if n == 0:
		print(result)

	for i in range(n):
		prefix = inp[0:i+1]

		if prefix in dic:

			if i == n:

				result += prefix
				print(result)

			wordBreakBackT(dic, inp[i+1:n], result  + prefix + ' ')

		

dic = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'and', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
inp = 'ailikeicecreamandmango'

#print(wordBreakDP(dic, inp))
#print(wordBreak(dic, inp))
wordBreakBackT(dic, inp, '')


#print('a' + ' ' + 'b')

