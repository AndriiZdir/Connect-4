def initializeGrid():
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    return grid;

def getColumn():
    pass
    
def newPiece(grid,col,piece):
    pass

def checkVictory (grid):
    pass

def checkFull(grid,col):
    if " " in grid[col]:
        return False;
    else:
        return True;
        
 
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
    P1 = "X"
    P2 = "O"
    newPiece(grid,1,P1)
    print grid
    newPiece(grid,2,P2)
    print grid
    newPiece(grid,3,P1)
    print grid
    newPiece(grid,4,P2)
    print grid
    newPiece(grid,5,P1)
    print grid
    newPiece(grid,6,P2)
    print grid
    newPiece(grid,7,P1)
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
    result = checkFull(grid,1)
    if result==True:
        print 'Passed'
    else:
        print "returned false when it should have returned true"
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    result = checkFull(grid,1)
    if result == False:
        print 'Passed'
    else:
        print "returned true when it should have returned false"
    
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
    

#test_initializeGrid()
#test_checkVictory()
#test_buildGrid()
#test_checkFull()
#test_findVacancy()
#test_newPiece()


