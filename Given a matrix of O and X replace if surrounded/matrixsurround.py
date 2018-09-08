def floodFillUtil(screen, x, y, prevC, newC):

    n = len(screen)    # Rows 
    m = len(screen[0]) # Columns
    
    # If x or y is outside screen, return
    if (x < 0 or x > n-1 or y < 0 or y > m-1):
        return screen

    # If color of screen[x][y] != as prevC, return
    if (screen[x][y] != prevC):
        return screen
    
    if (prevC == newC):
        return screen

    screen[x][y] = newC

    floodFillUtil(screen, x+1, y, prevC, newC)
    floodFillUtil(screen, x-1, y, prevC, newC)
    floodFillUtil(screen, x, y+1, prevC, newC)
    floodFillUtil(screen, x, y-1, prevC, newC)
    
    return screen
    
def floodFill(screen, x, y, newC):
    
    prevC = screen[x][y]
    return floodFillUtil(screen, x, y, prevC, newC)

def surr(mat):

    n = len(mat) #Filas
    m = len(mat[0]) #Columnas

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'O': mat[i][j] = '-'
                
    for j in range(m):
        if mat[0][j] == '-': mat = floodFill(mat, 0, j, 'O')
        
    for i in range(n):
        if mat[i][m-1] == '-': mat = floodFill(mat, i, m-1, 'O')
        
    for j in range(m):
        if mat[n-1][j] == '-': mat = floodFill(mat, n-1, j, 'O')

    for i in range(n):
        if mat[i][0] == '-': mat = floodFill(mat, i, 0, 'O')
            
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '-': mat[i][j] = 'X'

    return mat

mat = [['X','O','X','X','X','X'],
       ['X','O','X','X','O','X'],
       ['X','X','X','O','O','X'],
       ['O','X','X','X','X','X'],
       ['X','X','X','O','X','O'],
       ['O','O','X','O','O','O']]

mat2 = [['X','X','X','X'],
        ['X','O','X','X'],
        ['X','O','O','X'],
        ['X','O','X','X'],
        ['X','X','O','O']]

print(mat2)
print(surr(mat2))
