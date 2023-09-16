import numpy as np
import random
def get_ship_pos(x,y,ship_size,direction):
    ship_spots = []
    if direction == 0:
        for i in range(ship_size):
            ship_spots.append((x+i,y))
    elif direction == 1:
        for i in range(ship_size):
            ship_spots.append((x,y+i))
    return ship_spots

def pickStart():
    board = np.zeros((10, 10), dtype=int)
    ship_pos = []
    ships = [5, 3, 3, 2, 2]
    for ship in ships:
        board_possibilities, pos_possibilities = generateBoardStates(ship, board)
        board_index = random.choice(list(range(len(board_possibilities))))
        board = board_possibilities[board_index]
        pos = pos_possibilities[board_index]
        ship_pos.append(pos)

    return ship_pos

def generateBoardStates(shipSize, before_board):
    board_size = 10
    ship_sizes = [shipSize]
    board_states = []
    ship_spots = []
    
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
            #board_states.append(np.ravel(board.copy()))
            board_states.append(board.copy())
            return
        
        ship_size = remaining_ships[0]
        
        for x in [1,2,3,6,7,8]:
            for y in [1,2,3,6,7,8]:
                for direction in [0, 1]:
                    if is_valid_placement(board, ship_size, x, y, direction):
                        place_ship(board, ship_size, x, y, direction)
                        generate(board, remaining_ships[1:])
                        ship_spots.append(get_ship_pos(x,y,ship_size,direction))
                        remove_ship(board, ship_size, x, y, direction)
    
    generate(before_board, ship_sizes)
    
    return np.array(board_states), ship_spots


def getShipPos():
    '''
    THIS IS THE LIST OF SHIPS
    [5,3,3,2,2] 
    That is: 
    1x 5 long
    2x 3 long
    2x 2 long

    Your ships must satisfy this 
    '''

    # due to a bug we have the indexing of ships are 0-9
    shipPos = pickStart()
    # shipPos = [[(3,1), (4,1),(5,1)], 
    #             [(2,1),(2,2),(2,3),(2,4),(2,5)], 
    #             [(7,7),(8,7)] , 
    #             [(0,9), (1,9), (2,9)], 
    #             [(5,9), (6,9)]]
    return shipPos