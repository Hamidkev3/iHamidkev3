#A simple Tic-Tac-Toe of a course that I enjoyed

import random
import numpy as np
def create_board():
    return np.zeros((3,3), dtype=int)

board = create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

board = create_board()
place(board, 1, (0, 0))

def possibilities(board):
    return list(zip(*np.where(board == 0)))

possibilities(board)

random.seed(1)
def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

random_place(board, 2)


random.seed(1)
board = create_board()

for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print(board)

def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False

row_win(board, 1)

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False

diag_win(board, 2)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board ,player) == True or col_win(board ,player) == True or diag_win(board ,player) == True:
            return player
    else:
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    else: 
        winner = 0
    return winner
evaluate(board)

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_game() for i in range(1000)]
results.count(1)


random.seed(1)
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_strategic_game() for i in range(1000)]
results.count(1)



