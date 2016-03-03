import copy
# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.

transpositionTable = dict()

def minimax(node, depth, depthLimit, path):
    currPath = copy.deepcopy(path)
    """
    :param node:  a Game object responding to the following methods:
        str(): return a unique string describing the state of the game (for use in hash table)
        isTerminal(): checks if the game is at a terminal state
        successors(): returns a list of all legal game states that extend this one by one move
        isMinNode(): returns True if the node represents a state in which Min is to move
        isMaxNode(): returns True if the node represents a state in which Max is to move
    :return: the value of the game state
    """
    if node.isMaxNode():
        u = (currPath,-1000)
    else:
        u = (currPath,1000)
    
    #global transpositionTable
    #s = node.str()
    #Do we hit the depth limit? If so, we don't need to do any of this because
    #we are techincally 'done'.
    if (depth < depthLimit):
        #if s in transpositionTable:
        #    return transpositionTable[s]
        #elif node.isTerminal():
        if node.isTerminal():
            currPath.append(node)
            u = (currPath,node.utility())
            if u[1] is -1000:
                print 'd is broken'
        else:
            sucs = node.successors()
            currPath.append(node)
            vs = [minimax(c, depth+1, depthLimit, currPath) for c in sucs]
            if node.isMaxNode():
                for x in vs:
                    if u[1] <= x[1]:
                        #print u[1],' changed to ',x[1]
                        u = x
                        if u[1] is -1000:
                            print 'c is broken'
            elif node.isMinNode():
                for x in vs:
                    if u[1] >= x[1]:
                        u = x
                        if u[1] is -1000:
                            print 'b is broken'
            else:
                print("Something went horribly wrong")
                return None
    else:
        currPath.append(node)
        u = (currPath, node.estimateUtility())
        if u[1] is -1000:
            print 'a is broken'
    #transpositionTable[s] = u
    #print u[0].printBoard()
    return u
