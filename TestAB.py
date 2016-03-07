import Game
import time
from GameTreeSearchForward import minimax
from GameTreeSearchForwardAlphaBeta import minimaxAB

gameMode = "AI"
whosTurn = "Player"


#===========================================================================
#ENABLE TO TIME TRIAL THE AI // DISBLE TO RUN ONCE AND BE ABLE TO PLAY VS AI
#===========================================================================
TESTING = True


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

def chooseMode():
    mode = False
    global gameMode
    global whosTurn
    while mode is False:
        userIn = raw_input("Do you want to play, or let the AIs play? (Input either \"AI\" or \"Player\")\n")
        userIn.lower()
        #print mode
        if userIn.lower() == "ai":
            gameMode = "AI"
            mode = True
        elif userIn.lower() == "player":
            gameMode = "Player"
            mode = True
        else:
            print 'That is not a valid choice'
            mode = False
    turn = False
    if gameMode == "Player":
        while turn is False:
            userIn = raw_input("Who do you want to move first? (Input either \"AI\" or \"Player\")\n")
            #print turn
            if userIn == "AI":
                whosTurn = "AI"
                turn = True
            elif userIn == "Player":
                whosTurn = "Player"
                turn = True
            elif userIn == "player":
                whosTurn = "Player"
                turn = True
            elif userIn == "Ai":
                whosTurn = "AI"
                turn = True
            else:
                print 'That is not a valid input'
                turn = False

def runGame():
    a = Game.Game()

    if not TESTING:
        chooseMode()

    #For time trials
    start_time = time.time()

    if gameMode is 'AI':
        #Actualy infinity
        #alpha = -1*float("inf")
        #beta = float("inf")
        #Sufficiently large
        alpha = -1500
        beta = 1500

        transpositionTable = dict()
        while not a.isTerminal():
        #for x in range(1):
            transpositionTable.clear()
            path = []
            #without alpha-beta
            #b = minimax(a, 0, 5, path, transpositionTable)
            #With alpha-beta
            b = minimaxAB(a, 0, 8, path, alpha, beta, transpositionTable)
            if not (b[0])[0].isTerminal():
                #print b[1]
                a = (b[0])[1]
            a.printBoard()
            print '\n'

        finalUtil = a.utility()
        if finalUtil < 0:
            print '======================='
            print '======BLACK WINS======='
            print '======================='
        elif finalUtil > 0:
            print '======================='
            print '======WHITE WINS======='
            print '======================='
        else:
            print '======================='
            print '=========DRAW=========='
            print '======================='
    else:
        while not a.isTerminal():
        #for x in range(1):
            if a.isMaxNode() and (whosTurn is 'Player'):
                print 'Your Turn!'
                piece = False
                valid = False
                while not valid:
                    while not (type(piece) is tuple):
                        try:
                            #piece = tuple(map(int,raw_input().split(',')))
                            piece = tuple(int(x.strip()) for x in raw_input('Which piece do you want to move? (give in \"x,y\" format with (0,0 in top left))\n').split(','))
                        except (ValueError):
                            print 'Please input a proper tuple.'
                            continue

                        if type(piece) is not tuple:
                            print 'That is not a valid piece'
                            print type(piece)
                    direction = False
                    while not direction:
                        userIn = raw_input('What direction do you want to move it? (left/right/forward)\n')
                        #print type(userIn)
                        print userIn
                        if (userIn != 'left'):
                            if (userIn != 'right'):
                                if (userIn != 'forward'):
                                    print 'That is not a valid direction'
                                    direction = False
                                else:
                                    direction = True
                            else:
                                direction = True
                        else:
                            direction = True
                    valid = a.checkValidMove(userIn, piece[0],piece[1])
                    if not valid:
                        print 'That is not a valid move'
                        piece = False
                        direction = False

                a.movePiece(userIn,piece[0],piece[1])

                a.printBoard()
                print 'AIs Turn!'

                path = []
               # b = minimax(a, 0, 4, path)
                b = minimaxAB(a, 0, 4, path, alpha, beta, transpositionTable)
                if not (b[0])[0].isTerminal():
                    #print b[1]
                    a = (b[0])[1]
                a.printBoard()
                print '\n'

            elif a.isMaxNode() and (whosTurn is 'AI'):
                print 'AIs Turn!'

                path = []
                b = minimaxAB(a, 0, 4, path, alpha, beta, transpositionTable)
                if not (b[0])[0].isTerminal():
                    #print b[1]
                    a = (b[0])[1]
                a.printBoard()
                print '\n'

                print 'Your Turn!'
                piece = False
                valid = False
                while not valid:
                    while not (type(piece) is tuple):
                        try:
                            #piece = tuple(map(int,raw_input().split(',')))
                            piece = tuple(int(x.strip()) for x in raw_input('Which piece do you want to move? (give in \"x,y\" format with (0,0 in top left))\n').split(','))
                        except ValueError:
                            print 'Please input a proper tuple'
                            continue

                        if type(piece) is not tuple:
                            print 'That is not a valid piece'
                            print type(piece)
                    direction = False
                    while not direction:
                        userIn = raw_input('What direction do you want to move it? (left/right/forward)\n')
                        #print type(userIn)
                        print userIn
                        if (userIn != 'left'):
                            if (userIn != 'right'):
                                if (userIn != 'forward'):
                                    print 'That is not a valid direction'
                                    direction = False
                                else:
                                    direction = True
                            else:
                                direction = True
                        else:
                            direction = True
                    valid = a.checkValidMove(userIn, piece[0],piece[1])
                    if not valid:
                        print 'That is not a valid move'
                        piece = False
                        direction = False

                a.movePiece(userIn,piece[0],piece[1])

                a.printBoard()

            else:
                path = []
                b = minimaxAB(a, 0, 4, path, alpha, beta, transpositionTable)
                if not (b[0])[0].isTerminal():
                    #print b[1]
                    a = (b[0])[1]
                a.printBoard()
                print '\n'

        finalUtil = a.utility()
        if finalUtil < 0:
            print '======================='
            print '======BLACK WINS======='
            print '======================='
        elif finalUtil > 0:
            print '======================='
            print '======WHITE WINS======='
            print '======================='
        else:
            print '======================='
            print '=========DRAW=========='
            print '======================='

if __name__=='__main__':
    global averageTime
    global runCount

    if TESTING:
        #Change this number to # of trials
        runNumber = 1
        #initializes the time sum
        averageTime = 0
        #counts the runs performed
        runCount = 0
    else:
        #Run the game only once because not testing
        runNumber = 1


    #For each run
    for x in range(runNumber):
        if TESTING:
            #Start the timer for current run
            start_time = time.time()

        #Run the game
        runGame()

        if TESTING:
            #For time trials
            totalRuntime = time.time() - start_time
            #Print info for the trial we just ran
            print 'Runtime for trial #',x+1
            print("--- %s seconds ---" % (totalRuntime))
            #Add this run's time to total runtime
            averageTime = averageTime + totalRuntime
            #Increment the runs performed counter
            runCount += 1

    if TESTING:
        print '# of runs tested: ',runNumber
        print 'Average runtime for tests: ',averageTime/runCount