def wordBreak(dic, inp, result):
	
	n = len(inp)

	if n == 0:
		print(result)

	for i in range(n):
		prefix = inp[0:i+1]

		if prefix in dic:

			if i == n:

				result += prefix
				print(result)

			wordBreak(dic, inp[i+1:n], result  + prefix + ' ')

		

dic = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'and', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
inp = 'ilikeicecreamandmango'


wordBreak(dic, inp, '')
