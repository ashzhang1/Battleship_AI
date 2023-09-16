import random
import numpy as np

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    # x = random.randint(1,10)
    # y = random.randint(1,10)
    # return [x,y], storage
    
    if round > 1:

        # remove all boards from allBoardStates that do not fit the shot seqeunce.
        updateBoards(p1PrevHit, p1ShotSeq)
        
    updateProbabilities()
    
    return getMove(), storage 


def generateBoardStates():
    # Implement an algorithm to generate all possible states
    return np.empty


def updateBoards(prevHit, shotSeq):
    shot = shotSeq[-1]

    # Convert shot position to 1D-array index
    shotIndex = (shot[0] - 1) * 10 + shot[1] - 1
    
    boardValidity = list()

    # Update the list of valid placements
    for board in allBoardStates:
        cell = board[shotIndex]

        # Check if the cell matches the previous hit
        if(prevHit and cell != 1):
            boardValidity.append(False)
        elif(not prevHit and cell != 0):
            boardValidity.append(False)
        else:
            boardValidity.append(True)

    allBoardStates = allBoardStates[boardValidity]

# Generates probability density map
def updateProbabilities():
    map = np.zeros(100)
    for board in allBoardStates:
        map += board
    probabilityDensityMap = map

# Converts 1D-array index into Battleship game index
def getMove():
    index = np.argmax(probabilityDensityMap)
    #Handle tie
    x = int((index / 10)) + 1
    y = index % 10 + 1
    return [x, y]

allBoardStates = generateBoardStates()
probabilityDensityMap = np.zeros(100)


'''
Tasks:
1. Generate all valid boards --> ONLY done once.
    Figure out an algorithm to find all possible placements
2. Adding all cells of all the boards together --> ONLY done once.
3. Choose move based on the cell with highest count.
4a. Remove boards that don't fit the result from p1PrevHits.
    4b. Recalculate the sum of each cell of all the valid boards by substracting the result from 3a.
5. Repeat step 3 - 4.
'''
