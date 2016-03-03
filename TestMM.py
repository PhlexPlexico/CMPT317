import Game
from GameTreeSearchForward import minimax



#Tests that our coordinate system works with x and y properly
def testingCoords(a):
    print a.getPiece(0,0), " Expected B"
    print a.getPiece(0,1), " Expected B"
    print a.getPiece(0,2), " Expected B"
    print a.getPiece(0,3), " Expected B"
    print a.getPiece(0,4), " Expected B"
    print a.getPiece(0,5), " Expected B"
    
    print a.getPiece(5,5), " Expected W"
    print a.getPiece(5,4), " Expected W"
    print a.getPiece(5,3), " Expected W"
    print a.getPiece(5,2), " Expected W"
    print a.getPiece(5,1), " Expected W"
    print a.getPiece(5,0), " Expected W"

def whiteCheats(a):
    for x in range(6):
        a.setPiece(1,x,'W')
        a.setPiece(5,x,'.')
    


if __name__=='__main__':
    a = Game.Game()
    #whiteCheats(a)
    #Testing coords for reversal of x and y for array (funky shit messed us up on this)
    #testingCoords(a)
    
    #a.printBoard()
    #a.togglePlayer()
    #print(a.str())
    """
    a.setPiece(3,5,'B')
    a.setPiece(4,4,'W')
    a.setPiece(5,4,'.')
    a.setPiece(4,5,'W')
    a.setPiece(5,5,'.')
    """
    a.printBoard()
    
    while not a.isTerminal():
    #for x in range(1):
        path = []
        b = minimax(a, 0, 4, path)
        if not (b[0])[0].isTerminal():
            #print b[1]
            a = (b[0])[1]
        a.printBoard()
    