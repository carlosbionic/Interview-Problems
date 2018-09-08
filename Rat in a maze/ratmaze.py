def ratMaze(maze, x, y, n, sol):
	print(x,y)
	if x == n-1 and y == n-1:
		sol[x][y] = 1
		return True

	if x>=0 and x<n and y>=0 and y<n and maze[x][y]==1:
		sol[x][y] = 1

		if ratMaze(maze, x+1, y, n, sol) == True:
			return True

		if ratMaze(maze, x, y+1, n, sol) == True:
			return True

		sol[x][y] = 0
		return False


maze = [ [1, 0, 0, 0],
		 [1, 1, 1, 1],
		 [0, 1, 0, 0],
		 [1, 1, 1, 1] ]

sol = [[0 for j in range(4)] for i in range(4)]

ratMaze(maze, 0, 0, 4, sol)

for i in sol:
	for j in i:
		print(str(j) + " ", end="")
	print("")
