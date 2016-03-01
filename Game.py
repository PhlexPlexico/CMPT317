class Game:

    def __init__(self):
        self.gameBoard = [["." for x in range(6)] for y in range (6)]
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
        s = []
        w = self
        for x in range(6):
            for y in range(6):
                for z in range(3):
                    if self.checkValidMove('left',x,y):
                        if (self.turn is "Max" and self.getPiece(x,y) is "W") or (self.turn is "Min" and self.getPiece(x,y) is "W"):
                            w.movePiece('left',x,y)
                            s.append(w)
                            w = self
                    if self.checkValidMove('forward',x,y):
                        if (self.turn is "Max" and self.getPiece(x,y) is "W") or (self.turn is "Min" and self.getPiece(x,y) is "W"):
                            w.movePiece('forward',x,y)
                            s.append(w)
                            w = self
                    if self.checkValidMove('right',x,y):
                        if (self.turn is "Max" and self.getPiece(x,y) is "W") or (self.turn is "Min" and self.getPiece(x,y) is "W"):
                            w.movePiece('right',x,y)
                            s.append(w)
                            w = self
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
            
    def utility(self):
        """
        return: If white wins, return 1, if black wins, return -1, and if we do not find any return 0.
        """
        for x in range(6):
            if self.getPiece(x,0) is 'W':
                return 1
            elif self.getPiece(x,5) is 'B':
                return -1
        return 0
            
    def countWhite(self):
        count = 0
        for x in range(6):
            for y in range(6):
                if self.gameBoard[x][y] is 'W':
                    count += 1
        return count
        
        
    def countBlack(self):
        count = 0
        for x in range(6):
            for y in range(6):
                if self.gameBoard[x][y] is 'B':
                    count += 1
        return count
        
    def getPiece(self,x,y):
        return self.gameBoard[x][y]
        
    def setPiece(self, x,y,newPiece):
        self.gameBoard[x][y] = newPiece
        
    def checkValidMove(self,direction,x,y):
        if self.getPiece(x,y) is 'W':
            if y is not 0:
                if direction is 'left':
                    if x is 0:
                        return False
                    elif self.getPiece(x-1,y-1) is 'B':
                        return True
                    else:
                        return False
                elif direction is 'right':
                    if x is 5:
                        return False
                    elif self.getPiece(x-1,y+1) is 'B':
                        return True
                    else:
                        return False
                elif direction is 'forward':
                    if self.getPiece(x-1,y) is 'B':
                        return False
                    elif self.getPiece(x-1,y) is '.':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif self.getPiece(x,y) is 'B':
            if y is not 5:
                if direction is 'left':
                    if x is 0:
                        return False
                    elif self.getPiece(x+1,y-1) is 'W':
                        return True
                    else:
                        return False
                elif direction is 'right':
                    if x is 5:
                        return False
                    elif self.getPiece(x+1,y+1) is 'W':
                        return True
                    else:
                        return False
                elif direction is 'forward':
                    if self.getPiece(x+1,y) is 'W':
                        return False
                    elif self.getPiece(x+1,y) is '.':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def movePiece(self,direction,x,y):
        if self.getPiece(x,y) is 'W':
            if y is not 0:
                if direction is 'left':
                    if x is 0:
                        print 'That move is outside the board!'
                    elif self.getPiece(x-1,y-1) is 'B':
                        self.setPiece(x-1,y-1,'W')
                        self.setPiece(x,y,'.')
                    else:
                        print 'That is an invalid move!'
                elif direction is 'right':
                    if x is 5:
                        print 'That move is outside the board!'
                    elif self.getPiece(x-1,y+1) is 'B':
                        self.setPiece(x-1,y+1,'W')
                        self.setPiece(x,y,'.')
                    else:
                        print 'That is an invalid move!'
                elif direction is 'forward':
                    if self.getPiece(x-1,y) is 'B':
                        print 'there is a piece there!'
                    elif self.getPiece(x-1,y) is '.':
                        self.setPiece(x-1,y,'W')
                        self.setPiece(x,y,'.')
                    else:
                        
                        print 'That is an invalid move!'
                else:
                    print 'that is not a direction!'
            else:
                print 'We fucked up the code, chief!'
        elif self.getPiece(x,y) is 'B':
            if y is not 5:
                if direction is 'left':
                    if x is 0:
                        print 'That move is outside the board!'
                    elif self.getPiece(x+1,y-1) is 'W':
                        self.setPiece(x+1,y-1,'B')
                        self.setPiece(x,y,'.')
                    else:
                        print 'That is an invalid move!'
                elif direction is 'right':
                    if x is 5:
                        print 'That move is outside the board!'
                    elif self.getPiece(x+1,y+1) is 'W':
                        self.setPiece(x+1,y+1,'B')
                        self.setPiece(x,y,'.')
                    else:
                        print 'That is an invalid move!'
                elif direction is 'forward':
                    if self.getPiece(x+1,y) is 'W':
                        print 'there is a piece there!'
                    elif self.getPiece(x+1,y) is '.':
                        self.setPiece(x+1,y,'B')
                        self.setPiece(x,y,'.')
                    else:
                        print 'That is an invalid move!'
                else:
                    print 'that is not a direction!'
            else:
                print 'We fucked up the code, chief!'
        else:
            print 'That is not a piece on the board!'
        self.togglePlayer()
            
    def isTerminal(self):
        for x in range(6):
            if self.getPiece(x,0) is 'W':
                return True
            elif self.getPiece(x,5) is 'B':
                return True
        return False
        
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
        if self.isTerminal():
            print 'Game is Over! White hit terminal node.'
        print self.str()
    
    
if __name__=='__main__':
    x = Game()
    x.testGame()