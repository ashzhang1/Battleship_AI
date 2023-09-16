import random
import numpy as np


def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, storage):
    global heatMap, allStates, missedShots
    
    if round == 1:
        allStates = generateAllBoardStates()
        heatMap = generateHeatMap(allStates)
        return pickMove(heatMap), storage
    
    # Records missed shot coordinate
    if not p1PrevHit:
        missedShots.append(p1ShotSeq[-1])

    heatMap = updateHeatMap(p1PrevHit, p1ShotSeq[-1], heatMap)
    
    if not zerosHeatMap(heatMap):  
        return pickMove(heatMap), storage

    allStates = generateAllBoardStates()
    allStates = filterStates(allStates, missedShots)
    heatMap = generateHeatMap(allStates)
    heatMap = setZeros(heatMap, p1ShotSeq)
    return pickMove(heatMap)
    

def updateHeatMap(hit, lastShot, heatMap):
    '''
    Filter out invalid states based on the move and sum all remaining states
    '''
    pass  

def zerosHeatMap(heatMap):
    
    pass

def generateAllBoardStates():
    allStates = np.empty((0,100))
    ships = [5, 3, 3, 2, 2]
    for ship in ships:
        allStates = np.concatenate((allStates, generateBoardStates(ship)), 0)

    return allStates

def filterStates(allStates, missedShots):
    '''
    Set the cells to zero based on shot sequence
    '''
    pass

def generateHeatMap(allStates):
    '''
    Sum all states
    '''
    pass


def setZeros(heatMap, p1ShotSeq):
    '''
    Set the cells to zero based on shot sequence
    '''
    pass

def pickMove(heatMap):
    '''
    pick a cell with the highest value
    '''
    pass

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

#START:
allStates = None
heatMap = None
missedShots = list()
