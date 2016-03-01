class Pawn:
    
    colour = None
    
    def __init__(self, setColour):
        self.colour = setColour
        
    def getColour(self):
        return self.colour