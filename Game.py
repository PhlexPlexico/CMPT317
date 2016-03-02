import copy
class Game:

    def __init__(self):
        self.gameBoard = [["." for y in range(6)] for x in range (6)]
        for x in range(6):
            self.gameBoard[0][x] = 'B'
            self.gameBoard[5][x] = 'W'
            
        self.turn = 'Max'
        
    def togglePlayer(self):
        if self.turn is 'Max':
            self.turn = 'Min'
        else:
            self.turn = 'Max'
            
    def printBoard(self):
        for x in range(6):
            print self.gameBoard[x]
            
    def successors(self):
        #print 'ABOUT TO SUCCESSORS'
        s = []
        #print 'KAY WE GOT AN EMPTY LIST'
        w = copy.deepcopy(self)
        #w = self
        #print 'WE COPIED IT, DOES IT WORK?'
        #print w.str()
        for y in range(6):
            for x in range(6):
                if self.checkValidMove('left',y,x):
                    if self.turn is 'Max' and self.getPiece(y,x) is 'W':
                        w.movePiece('left',y,x)
                        #Debugging
                        #print w.str()
                        s.append(w)
                        w = copy.deepcopy(self)
                    if self.turn is 'Min' and self.getPiece(y,x) is 'B':
                        w.movePiece('left',y,x)
                        print w.str()
                        s.append(w)
                        w = copy.deepcopy(self)   
                if self.checkValidMove('forward',y,x):
                    if self.turn is 'Max' and self.getPiece(y,x) is 'W':
                        #Debugging
                        #print 'DOES THIS LOGIC WORK!?!?!?!?!?!?!?!?!'
                        w.movePiece('forward',y,x)
                        #Debugging
                        #print w.str()
                        s.append(w)
                        #Debugging
                        #print s
                        w = copy.deepcopy(self)
                    if self.turn is 'Min' and self.getPiece(y,x) is 'B':
                        w.movePiece('forward',y,x)
                        #Debugging
                        #print w.str()
                        s.append(w)
                        w = copy.deepcopy(self) 
                if self.checkValidMove('right',y,x):
                    if self.turn is 'Max' and self.getPiece(y,x) is 'W':
                        w.movePiece('right',y,x)
                        #Debugging
                        #print w.str()
                        s.append(w)
                        w = copy.deepcopy(self)
                    if self.turn is 'Min' and self.getPiece(y,x) is 'B':
                        w.movePiece('right',y,x)
                        #Debugging
                        #print w.str()
                        s.append(w)
                        w = copy.deepcopy(self)
        print "\nHere is the boards for successors\n"
        for x in s:
            #print "Here is a successor: ", x.str()
            #print "\n"
            x.printBoard()
            print "\n"
        return s
            
    #def allBlanks(self):
        """
        :return: a list of available places to put a marker
        """
    #    return [v for v in self.gameBoard if self.gameBoard[v] == ' ']
            
    def isMinNode(self):
        if self.turn is 'Min':
            return True
        else:
            return False
            
    def isMaxNode(self):
        if self.turn is 'Max':
            return True
        else:
            return False
            
    """
    Function for utility, in checking on who wins.
    """
    def utility(self):
        """
        return: If white wins, return 1, if black wins, return -1, and if we do not find any return 0.
        """
        for x in range(6):
            if self.getPiece(0,x) is 'W':
                return 1000
            elif self.getPiece(5,x) is 'B':
                return -1000
        return 0
        
    def estimateUtility(self):
        x = 0
        y = 0
        #Check entire board
        for i in range(6):
            for j in range(6):
                #If piece found, give 17 utility to the player for the 
                #piece being alive, plus 7 utility per space moved for that piece
                if self.getPiece(i,j) is 'W':
                    x += 17
                    x += 7*(5-i)
                elif self.getPiece(i,j) is 'B':
                    y += 17
                    y += 7*i
        #Utility = positive utility of white plus negative utility of black
        u = x - y
        return u
        
    """
    Function used to count how many pieces are currently on the board that are white.
    return: the count of white pieces on the board.
    """
    def countWhite(self):
        count = 0
        for x in range(6):
            for y in range(6):
                if self.gameBoard[y][x] is 'W':
                    count += 1
        return count
        
    """
    Function used to count how many pieces are currently on the board that are black.
    return: the count of black pieces on the board.
    """
    def countBlack(self):
        count = 0
        for x in range(6):
            for y in range(6):
                if self.gameBoard[y][x] is 'B':
                    count += 1
        return count
        
    def getPiece(self,y,x):
        return self.gameBoard[y][x]
        
    def setPiece(self, y,x,newPiece):
        self.gameBoard[y][x] = newPiece
    """
    Function used to check for a valid move. Used by successor function for the AI.
    The user should not be using this?
    Param: self the game object.
    Param: direction, where the person or ai wishes to move (left, right, up, down).
    Param: x, the x value of the board.
    Param: y, the y value of the board.
    """
    def checkValidMove(self,direction,y,x):
        if self.getPiece(y,x) is 'W':
            if y is not 0:
                if direction is 'left':
                    if x is 0:
                        return False
                    elif self.getPiece(y-1,x-1) is 'B':
                        return True
                    else:
                        return False
                elif direction is 'right':
                    if x is 5:
                        return False
                    elif self.getPiece(y-1,x+1) is 'B':
                        return True
                    else:
                        return False
                elif direction is 'forward':
                    if self.getPiece(y-1,x) is 'B':
                        return False
                    elif self.getPiece(y-1,x) is '.':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif self.getPiece(y,x) is 'B':
            if y is not 5:
                if direction is 'left':
                    if x is 0:
                        return False
                    elif self.getPiece(y+1,x-1) is 'W':
                        return True
                    else:
                        return False
                elif direction is 'right':
                    if x is 5:
                        return False
                    elif self.getPiece(y+1,x+1) is 'W':
                        return True
                    else:
                        return False
                elif direction is 'forward':
                    if self.getPiece(y+1,x) is 'W':
                        return False
                    elif self.getPiece(y+1,x) is '.':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    """
    Function used to check for a moving a piece.
    The user should be using this?
    Param: self the game object.
    Param: direction, where the person or ai wishes to move (left, right, up, down).
    Param: x, the x value of the board.
    Param: y, the y value of the board.
    """
    def movePiece(self,direction,y,x):
        toggle = False
        if self.getPiece(y,x) is 'W':
            if y is not 0:
                if direction is 'left':
                    if x is 0:
                        print 'That move is outside the board!'
                        toggle = True
                    elif self.getPiece(y-1,x-1) is 'B':
                        self.setPiece(y-1,x-1,'W')
                        self.setPiece(y,x,'.')
                        print 'white moves left'
                    else:
                        print 'That is an invalid move!'
                        toggle = True
                elif direction is 'right':
                    if x is 5:
                        print 'That move is outside the board!'
                        toggle = True
                    elif self.getPiece(y-1,x+1) is 'B':
                        self.setPiece(y-1,x+1,'W')
                        self.setPiece(y,x,'.')
                        print 'white moves right'
                    else:
                        print 'That is an invalid move!'
                        toggle = True
                elif direction is 'forward':
                    if self.getPiece(y-1,x) is 'B':
                        print 'there is a piece there!'
                        toggle = True
                    elif self.getPiece(y-1,x) is '.':
                        self.setPiece(y-1,x,'W')
                        self.setPiece(y,x,'.')
                        print 'white moves forward'
                    else:
                        
                        print 'That is an invalid move!'
                        toggle = True
                else:
                    print 'that is not a direction!'
                    toggle = True
            else:
                print 'We fucked up the code, chief! White'
                toggle = True
        elif self.getPiece(y,x) is 'B':
            if y is not 5:
                if direction is 'left':
                    if x is 0:
                        print 'That move is outside the board!'
                        toggle = True
                    elif self.getPiece(y+1,x-1) is 'W':
                        self.setPiece(y+1,x-1,'B')
                        self.setPiece(y,x,'.')
                        print 'black moves left'
                    else:
                        print 'That is an invalid move!'
                        toggle = True
                elif direction is 'right':
                    if x is 5:
                        print 'That move is outside the board!'
                        toggle = True
                    elif self.getPiece(y+1,x+1) is 'W':
                        self.setPiece(y+1,x+1,'B')
                        self.setPiece(y,x,'.')
                        print 'black moves right'
                    else:
                        print 'That is an invalid move!'
                        toggle = True
                elif direction is 'forward':
                    if self.getPiece(y+1,x) is 'W':
                        print 'there is a piece there!'
                        toggle = True
                    elif self.getPiece(y+1,x) is '.':
                        self.setPiece(y+1,x,'B')
                        self.setPiece(y,x,'.')
                        print 'black moves forward'
                    else:
                        print 'That is an invalid move!'
                        toggle = True
                else:
                    print 'that is not a direction!'
                    toggle = True
            else:
                print 'We fucked up the code, chief! Black'
                toggle = True
        else:
            print 'That is not a piece on the board!'
            toggle = True
        self.togglePlayer()
            
    """
    Check if the current node is terminal, if one is, the game is over.
    return: true if white or black make it, false otherwise.
    """
    def isTerminal(self):
        for x in range(6):
            if self.getPiece(0,x) is 'W':
                return True
            elif self.getPiece(5,x) is 'B':
                return True
            elif self.successors() is None:
                return True
        return False
        
    """
    A string function for the gameboard.
    Return: the string value of the current gameboard. Used for search.
    """
    def str(self):
        s = ''
        for i in range(6):
            for j in range(6):
                s += self.getPiece(i,j)
        return s
    
    def testGame(self):
        self.printBoard()
        self.movePiece('forward',5,5)
        self.printBoard()
        self.movePiece('forward',4,5)
        self.printBoard()
        self.movePiece('forward',3,5)
        self.printBoard()
        self.movePiece('forward',2,5)
        self.printBoard()
        self.movePiece('left',1,5)
        self.printBoard()
        #self.successors()
        if self.isTerminal():
            print 'Game is Over! White hit terminal node.'
        print self.str()
    
    
if __name__=='__main__':
    x = Game()
    x.successors()
    x.printBoard()
    #x.testGame()
    