# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.

transpositionTable = dict()

def minimax(node, depth, depthLimit):
    """
    :param node:  a Game object responding to the following methods:
        str(): return a unique string describing the state of the game (for use in hash table)
        isTerminal(): checks if the game is at a terminal state
        successors(): returns a list of all legal game states that extend this one by one move
        isMinNode(): returns True if the node represents a state in which Min is to move
        isMaxNode(): returns True if the node represents a state in which Max is to move
    :return: the value of the game state
    """
    global transpositionTable
    s = node.str()
    #Do we hit the depth limit? If so, we don't need to do any of this because
    #we are techincally 'done'.
    if (depth < depthLimit):
        if s in transpositionTable:
            return transpositionTable[s]
        elif node.isTerminal():
            #original
            #u = node.utility()
            u = (node,node.utility())
        else:
            sucs = node.successors()
            vs = [minimax(c, depth+1, depthLimit) for c in sucs]
            if node.isMaxNode():
                for x in len(vs):
                    if u[1] <= (vs[x])[1]:
                        u = (sucs[x],vs[x])
            elif node.isMinNode():
                for x in len(vs):
                    if u[1] >= (vs[x])[1]:
                        u = (sucs[x],vs[x])
            else:
                print("Something went horribly wrong")
                return None
    else:
        u = (node, node.estimateUtility())
    transpositionTable[s] = u
    return u
