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
            ## Oops -- are you sure you want to return the column as a
            ## string? -- TH
           column = answer
           return column;
       
def newPiece(grid,col,piece):
    #help from mac
    t = 5
    ## this should work, but it's inelegant and risky to have the
    ## relationship between t=5 and range(6) not made explicit (also,
    ## it's not clear to me what "t" is supposed to stand for -- try
    ## to use meaningful variable names. -- TH
    for y in range(6):
        if grid[col][t] == " ":
            grid[col][t] = piece
            print grid[col]
            return;            
        else:
            t-=1

def checkVictory(grid,piece):
    ## It seems like you could significantly simplify the logic
    ## here. -- TH.
    #check column
    for col in range(7):
        print grid[col]
        for row in range(6):
            x=0
            for y in range(4):
                if row>2:
                    if grid[col][row] == grid[col][row-y] and grid[col][row]==piece:
                        x+=1
                else:
                    if grid[col][row] == grid[col][row+y] and grid[col][row]== piece:
                        x+=1
                if x == 4:
                    return True;
    
    
            
                    
                

def checkFull(grid,col):
    if " " in grid[col]:
        return False;
    else:
        return True;
        
 
def buildGrid(grid):
    #builds the visual for the game
    #pretty confused as to how this works, it just ended up working, and it's not too important anyways.
    for row in range(6):
        for col in range(7):
            print "| " + grid[col][row],
        print "|"
        print"_____________________________"
            

## It looks like the function below is nearly identical to CheckFull,
## no? Why implement the logic twice?
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
    grid = [[" "," "," "," "," "," "],[" "," "," "," "," ","O"],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    P1 = "X"
    P2 = "O"
    newPiece(grid,0,P1)
    
    newPiece(grid,1,P2)
    #print grid
    newPiece(grid,2,P1)
    #print grid
    newPiece(grid,3,P2)
    #print grid
    newPiece(grid,4,P1)
    #print grid
    newPiece(grid,5,P2)
    #print grid
    newPiece(grid,6,P1)
    #print grid

def test_checkVictory():
    P1 = "X"
    grid=[[" "," "," "," "," "," "],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #row=checkVictory(grid)
    #print row
    grid=[[" "," "," "," "," "," "],[" "," "," ","X","X","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," ","X","X","X","X"],[" "," "," "," "," "," "]]
    col = checkVictory(grid,P1)
    print col
    grid = [[" "," "," "," "," ","X"],[" "," "," "," ","X"," "],[" "," "," ","X"," "," "],[" "," ","X"," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #upDiag = checkVictory(grid)
    #print upDiag
    grid = [[" "," ","X"," "," "," "],[" "," "," ","X"," "," "],[" "," "," "," ","X"," "],[" "," "," "," "," ","X"],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
    #downDiag = checkVictory(grid)
    #print downDiag
    grid=[[" ","X"," ","X"," ","X"],["X"," ","X"," ","X"," "],[" ","X"," ","X"," ","X"],["X"," ","X"," ","X"," "],[" ","X"," ","X"," ","X"],["X"," ","X"," ","X"," "],[" ","X"," ","X"," ","X"]]

    
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
    

test_initializeGrid()
test_checkVictory()
test_buildGrid()
test_checkFull()
test_findVacancy()
test_newPiece()
test_getColumn()

