import random
import numpy as np


def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    global heatMap, currentAllStates, missedShots

    print(f'num shots: {len(p1ShotSeq)}')
    if len(p1ShotSeq) != 0:
        print(f'PREV SHOT: {p1ShotSeq[-1]}')

    if len(p1ShotSeq) == 0:
        currentAllStates = generateAllBoardStates()
        heatMap = generateHeatMap(currentAllStates)
        return pickMove(heatMap), storage

    # Records missed shot coordinate
    if not p1PrevHit:
        missedShots.append(p1ShotSeq[-1])

    currentAllStates = updateStates(p1PrevHit, p1ShotSeq[-1], currentAllStates)
    heatMap = generateHeatMap(currentAllStates)
    index = (p1ShotSeq[-1][0] - 1) * 10 + p1ShotSeq[-1][1] - 1
    heatMap[index] = 0
    heatMap = setZeros(heatMap, p1ShotSeq)
    if not zerosHeatMap(heatMap):
        return pickMove(heatMap), storage

    currentAllStates = generateAllBoardStates()
    currentAllStates = filterStates(currentAllStates, missedShots)
    heatMap = generateHeatMap(currentAllStates)
    heatMap = setZeros(heatMap, p1ShotSeq)
    return pickMove(heatMap), storage
    

def updateStates(hit, lastShot, currentAllStates):
    validity = [True] * len(currentAllStates)
    index = (lastShot[0] - 1) * 10 + lastShot[1] - 1
    for i in range(len(currentAllStates)):
        if hit and (currentAllStates[i][index] != 1):
            validity[i] = False
        if (not hit) and (currentAllStates[i][index] != 0):
            validity[i] = False
    return currentAllStates[validity]
      
def zerosHeatMap(heatMap):
    # print(f"HEATMAP WHEN ALL ZEROS:\n{heatMap}")
    # print(f'ALL ZEROS OUTPUT: {np.all(heatMap == 0)}')
    return np.all(heatMap == 0)

def generateAllBoardStates():
    currentAllStates = np.empty((0,100))
    ships = [5, 3, 3, 2, 2]
    for ship in ships:
        currentAllStates = np.concatenate((currentAllStates, generateBoardStates(ship)), 0)
    return currentAllStates

def filterStates(currentAllStates, missedShots):
    '''
    Set the cells to zero based on shot sequence
    '''
    validity = [True] * len(currentAllStates)
    for missedShot in missedShots:
        index = (missedShot[0] - 1) * 10 + missedShot[1] - 1
        for i in range(len(currentAllStates)):
            if currentAllStates[i][index] != 0:
                validity[i] = False
    return currentAllStates[validity]

def generateHeatMap(currentAllStates):
    '''
    Sum all states
    '''
    map = np.zeros(100)
    for state in currentAllStates:
        map += state
    return map

def setZeros(heatMap, p1ShotSeq):
    '''
    Set the cells to zero based on shot sequence
    '''
    for shot in p1ShotSeq:
        index = (shot[0] - 1) * 10 + shot[1] - 1
        heatMap[index] = 0
    return heatMap
    
def pickMove(heatMap):
    '''
    pick a cell with the highest value
    heatMap: 1D Numpy Array
    '''
    index = np.argmax(heatMap)
    x = int((index / 10)) + 1
    y = index % 10 + 1
    print(f'MY SHOT: {[x,y]}')
    print(f'HEATMAP: \n{heatMap.reshape((10, 10))}')
    return [x, y]

def generateBoardStates(shipSize):
    board_size = 10
    ship_sizes = [shipSize]
    board_states = []
    
    def is_valid_placement(board, size, x, y, direction):
        if direction == 0:
            return x + size <= board_size and np.all(board[y, x:x+size] == 0)
        elif direction == 1:
            return y + size <= board_size and np.all(board[y:y+size, x] == 0)
        return False
    
    def place_ship(board, size, x, y, direction):
        if direction == 0:
            board[y, x:x+size] = 1
        elif direction == 1:
            board[y:y+size, x] = 1
    
    def remove_ship(board, size, x, y, direction):
        if direction == 0:
            board[y, x:x+size] = 0
        elif direction == 1:
            board[y:y+size, x] = 0
    
    def generate(board, remaining_ships):
        if not remaining_ships:
            board_states.append(np.ravel(board.copy()))
            return
        
        ship_size = remaining_ships[0]
        
        for x in range(board_size):
            for y in range(board_size):
                for direction in [0, 1]:
                    if is_valid_placement(board, ship_size, x, y, direction):
                        place_ship(board, ship_size, x, y, direction)
                        generate(board, remaining_ships[1:])
                        remove_ship(board, ship_size, x, y, direction)
    
    empty_board = np.zeros((board_size, board_size), dtype=int)
    generate(empty_board, ship_sizes)
    
    return np.array(board_states)

# Initialising global variables
currentAllStates = None
heatMap = None
missedShots = list()
