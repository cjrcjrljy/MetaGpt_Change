import random

def initialize_board():
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    board[i][j] = 2 if random.random() < 0.9 else 4

def compress(board):
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    new_board = []
    for i in range(4):
        new_board.append(board[i][::-1])
    return new_board

def transpose(board):
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return new_board

def move_left(board):
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def get_current_state(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if board[3][j] == board[3][j + 1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if board[i][3] == board[i + 1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

def print_board(board):
    for i in range(4):
        print('+----' * 4 + '+')
        print('|'.join(f'{board[i][j]:4}' if board[i][j] != 0 else '    ' for j in range(4)) + '|')
    print('+----' * 4 + '+')

def start_game():
    board = initialize_board()
    print_board(board)
    game_state = 'GAME NOT OVER'

    while game_state == 'GAME NOT OVER':
        move = input('Enter move (w/a/s/d): ')
        if move == 'w':
            board = move_up(board)
            add_new_tile(board)
        elif move == 's':
            board = move_down(board)
            add_new_tile(board)
        elif move == 'a':
            board = move_left(board)
            add_new_tile(board)
        elif move == 'd':
            board = move_right(board)
            add_new_tile(board)
        else:
            print('Invalid move. Please enter w, a, s, or d.')
            continue

        print_board(board)
        game_state = get_current_state(board)

    if game_state == 'WON':
        print('Congratulations! You have won the game!')
    else:
        print('Game over. You have lost the game.')

if __name__ == '__main__':
    start_game()