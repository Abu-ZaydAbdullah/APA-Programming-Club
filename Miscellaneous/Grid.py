from math import floor
class Grid :
    width = 3;
    length = width * width;
    grid = [[6,7,0, 0,4,0, 9,0,1],
            [1,0,0, 0,5,0, 0,0,0],
            [0,0,0, 3,0,0, 4,0,6],
                    
            [0,0,9, 0,3,0, 0,0,0],
            [3,1,0, 5,6,8, 0,4,9],
            [0,0,0, 0,7,0, 5,0,0],
            
            [4,0,6, 0,0,1, 0,0,0],
            [0,0,0, 0,2,0, 0,0,8],
            [8,0,3, 0,9,0, 0,1,4],
            ]
    def isEmpty(row, column):
        return Grid.grid[row][column] == 0
    
    def inRow(value, row):
        for i in Grid.grid[row]:
            if i == value:
                return True
        return False
    
    def inColumn(value, column):
        for i in range(Grid.length):
            if Grid.grid[i][column] == value:
                return True
        return False

    def inSquare(value, square):
        for i in range(Grid.length):
            for j in range(Grid.length):
                if (Grid.mapSquare(i, j) == square) and (Grid.grid[i][j] == value):
                    return True
        return False
    
    def mapSquare(cRow, cColumn):
        row = floor(cRow/3)
        column = floor(cColumn/3)
        return row* Grid.width + column
    
    def isValid(value, row, column):
        isEmpty = Grid.isEmpty(row, column)
        inRow = Grid.inRow(value, row)
        inColumn = Grid.inColumn(value, column)
        inSquare = Grid.inSquare(value, Grid.mapSquare(row,column))
        return not inRow and not inColumn and not inSquare and isEmpty

    def topLeft(square):
        arr = [0,0]
        arr[0] = floor(square/3)*3
        arr[1] = (square - arr[0])*3
        return arr
    
    def numberOfValid(value, square):
        row = Grid.topLeft(square)[0]
        column = Grid.topLeft(square)[1]
        count = 0
        for i in range(row, row + Grid.width):
            for j in range(column, column + Grid.width):
                if Grid.isValid(value, i, j):
                    count += 1
        return count
    def put(value, square):
        row = Grid.topLeft(square)[0]
        column = Grid.topLeft(square)[1]
        for i in range(row, row + Grid.width):
            for j in range(column, column + Grid.width):
                if Grid.isValid(value, i, j):
                    Grid.grid[i][j] = value
                    
    def solveSquare(square):
        for i in range(1, Grid.length+1):
            if Grid.numberOfValid(i, square) == 1:
                Grid.put(i, square)
                
    def solved():
        for i in Grid.grid:
            for j in i:
                if j == 0:
                    return False
        return True
    
    def solve():
        while not Grid.solved():
            for i in range(Grid.length):
                Grid.solveSquare(i)

    def printSquare(square):
        row = Grid.topLeft(square)[0]
        column = Grid.topLeft(square)[1]
        txt = ""
        for i in range(row, row+3):
            for i in range(column, column+3):
                txt += Grid.gridi[i][j]
            txt += "\n"
        return txt
    
    def __str__(self):
        txt = ""
        for i in range(Grid.length):
            for j in range(Grid.length):
                txt += str(Grid.grid[i][j])
                if (j+1) % 3 == 0:
                    txt += " "
            txt += "\n"
            if (i+1) % 3 == 0:
                txt += "\n"
        return txt
    
test = Grid()
test.solve();
print(test)
