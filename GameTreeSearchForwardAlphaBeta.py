import copy
import math
# The search space is a tree, but the state space is a graph: there may be several different ways to
# reach a given game state.  The transposition table is a dictionary (hash table) that remembers if
# a game state was seen before, and it it was, what its minimax value is.


def minimaxAB(node, depth, depthLimit, path, alpha, beta, transpositionTable):
    currPath = copy.deepcopy(path)
    currPath.append(node)
    
    if node.isMaxNode():
        u = (currPath,-1000)
    else:
        u = (currPath,1000)
        
    s = node.str()
    
    #Do we hit the depth limit? If so, we don't need to do any of this because we are techincally 'done'.
    if (depth < depthLimit):
        if s in transpositionTable:
            return transpositionTable[s]
        if node.isTerminal():
            u = (currPath,node.utility())
        else:
            #Get a list of successors to current game state
            sucs = node.successors()
            #vs is the list of all tuples (path,utility) returned from running minimax on successors
            vs = [minimaxAB(c, depth+1, depthLimit, currPath, alpha, beta, transpositionTable) for c in sucs]
            if node.isMaxNode():
                #Actual infinity
                #u = (u[0],-1*float("inf"))
                #Sufficiently large
                u = (u[0],-1500)
                
                #For all successors
                for x in vs:
                    #If current best utility is <= utility of current successor
                    if u[1] <= x[1]:
                        #set the best route to the current successor
                        u = x
                        #If the best route is greater utility than beta, return, because we're pruning this
                        if u[1] >= beta:
                            return u
                        #else set alpha to the max of alpha and the best route so far's utility
                    alpha = max(alpha,u[1])
            elif node.isMinNode():
                #Actual infinity
                #u = (u[0],float("inf"))
                #Sufficiently large
                u = (u[0],1500)
                
                for x in vs:
                    #If current best utility is >= utility of current successor
                    if u[1] >= x[1]:
                        #set the best route to the current successor
                        u = x
                        #If the best route is greater utility than beta, return, because we're pruning this
                        if u[1] <= alpha:
                            return u
                        #else set beta to the min of beta and the best route so far's utility
                    beta = min(beta,u[1])
            else:
                print("Something went horribly wrong")
                return None
    else:
        #if depth limit reached, return estimate of current node's utility
        u = (currPath, node.estimateUtility())
    transpositionTable[s] = u
    return u
    