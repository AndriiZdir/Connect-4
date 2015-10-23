def initializeGrid():
    pass

def getColumn():
    pass

def newPiece(grid,col):
    pass

def checkVictory (grid):
    pass

def checkFull(grid, col):
    pass

def buildGrid(grid):
    pass

def findVacancy(grid, col):
    pass




def test_initializeGrid():
    grid = initializeGrid()
    print (grid)

def test_getColumn():
    column = getColumn()
    print (column)

def test_newPiece():
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

    newPiece(1,grid)
    print grid
    newPiece(2,grid)
    print grid
    newPiece(3,grid)
    print grid
    newPiece(4,grid)
    print grid
    newPiece(5,grid)
    print grid
    newPiece(6,grid)
    print grid
    newPiece(7,grid)
    print grid

def test_checkVictory():
    grid=[[" "," "," "," "," "," "],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    row=checkVictory(grid)
    print row
    grid=[[" "," "," "," "," "," "],[" "," ","X ","X ","X ","X "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    col = checkVictory(grid)
    print col
    grid = [[" "," "," "," "," ","X"],[" "," "," "," ","X"," "],[" "," "," ","X"," "," "],[" "," ","X"," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    upDiag = checkVictory(grid)
    print upDiag
    grid = [[" "," ","X"," "," "," "],[" "," "," ","X"," "," "],[" "," "," "," ","X"," "],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    downDiag = checkVictory(grid)
    print downDiag
def test_checkFull():
    grid=[[" "," "," "," "," "," "],["X","X","O","X","O","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    checkFull(grid,1)
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    checkFull(grid,2)
    
def test_buildGrid():
    grid = [["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
    buildGrid(grid)
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    buildGrid(grid)
    
def test_findVacancy():
    grid = [["X","X","X","X","X","X"],["X","X","X","X","X","X"],[" "," ","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
    vacant = findVacancy(grid,3)
    if vacant == True:
        print "works when there is a vacancy"
    else:
        print "doesn't work when there is a vacancy"
    grid = [["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
    vacant = findVacancy(grid,3)
    if vacant == False:
        print "works when it is full"
    else:
        print "doesn't work when it is full"
    

test_initializeGrid
test_checkVictory()
test_buildGrid()
test_checkFull()
test_findVacancy()
test_newPiece()


