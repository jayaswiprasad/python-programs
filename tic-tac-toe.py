def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('-------------')

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def get_move(player, board):
    while True:
        move = input(f"{player}'s turn. Enter coordinates (row,col) to place {player}: ")
        row, col = move.split(',')
        if not row.isdigit() or not col.isdigit():
            print('Invalid input. Please enter two numbers separated by a comma.')
            continue
        row, col = int(row), int(col)
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid coordinates. Please enter two numbers between 0 and 2.')
            continue
        if board[row][col] != ' ':
            print('That spot is already taken. Please choose another spot.')
            continue
        return row, col

def play_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = players[0]
    print_board(board)
    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f'{winner} wins!')
            return
        if all([cell != ' ' for row in board for cell in row]):
            print('Tie game!')
            return
        current_player = players[(players.index(current_player) + 1) % len(players)]

play_game()
