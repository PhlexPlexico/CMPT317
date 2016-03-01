import Game
from GameTreeSearch import minimax



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
    
    a.printBoard()
    #a.togglePlayer()
    #print(a.str())
    print(minimax(a))
    #print(minimax(b))