def initializeGrid():
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    return grid;

def getColumn():
    #help from mac to get this to work
    column=0
    while column == 0:
        answer = raw_input('What column do you want between 1-7')
        if int(answer) > 7:
            print('Too high')
        elif int(answer) < 1:
            print('Too low')
        else:
           column = answer
           return column;
       
def newPiece(grid,col,piece):
    #idk how to change a specific character in one list
    grid[col] = 'X'
    

def checkVictory (grid):
    pass

def checkFull(grid,col):
    if " " in grid[col]:
        return False;
    else:
        return True;
        
 
def buildGrid(grid):
    for col in range(7):
        print
        for row in range(6):
            print "|"+grid[col][row]
        print "|"
        print "_________________________",


def findVacancy(grid, col):
    '''Return True if there is a vacancy in column col of grid.'''
    if ' ' in grid[col]:  
        print('There is a space')
        return True
    else:
        print('No space')
        return False




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
    vacant = findVacancy(grid,2)
    if vacant == True:
        print "works when there is a vacancy"
    else:
        print "doesn't work when there is a vacancy"
    grid = [["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"],["X","X","X","X","X","X"]]
    vacant = findVacancy(grid,2)
    if vacant == False:
        print "works when it is full"
    else:
        print "doesn't work when it is full"
    

#test_initializeGrid()
#test_checkVictory()
test_buildGrid()
#test_checkFull()
#test_findVacancy()
#test_newPiece()
#test_getColumn()

