def initializeGrid():
    pass

def getColumn():
    pass

def newPiece():
    pass

def checkVictory():
    pass

def checkFull():
    pass

def buildGrid():
    pass

def findVacancy():
    pass




def test_initializeGrid():
	grid = initializeGrid
	print (grid)

def test_getColumn():
	column = getColumn
	print (column)

def test_newPiece():
	newPiece(1)
        print grid
	newPiece(2)
        print grid
	newPiece(3)
        print grid
	newPiece(4)
        print grid
	newPiece(5)
        print grid
	newPiece(6)
        print grid
	newPiece(7)
        print grid

def test_checkVictory():
    grid=[[" "," "," "," "," "," "],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #row=checkVictory(grid)
    #print row
    grid=[[" "," "," "," "," "," "],[" "," ","X ","X ","X ","X "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #col = checkVictory(grid)
    #print col
    grid = [[" "," "," "," "," ","X"],[" "," "," "," ","X"," "][" "," "," ","X"," "," "],[" "," ","X"," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #upDiag = checkVictory(grid)
    #print upDiag
    grid = [[" "," ","X"," "," "," "],[" "," "," ","X"," "," "],[" "," "," "," ","X"," "],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #downDiag = checkVictory(grid)
    #print downDiag
def test_checkFull():
    grid=[[" "," "," "," "," "," "],["X","X","O","X","O","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    checkFull(grid)
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    checkFull(grid)
    
def test_buildGrid():
    pass

def find_findVacancy():
    pass
