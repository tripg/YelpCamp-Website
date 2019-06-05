
def display_board(board):

    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def place_marker(board,marker,position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  
            (board[4] == mark and board[5] == mark and board[6] == mark) or  
            (board[1] == mark and board[2] == mark and board[3] == mark) or 
            (board[7] == mark and board[4] == mark and board[1] == mark) or  
            (board[8] == mark and board[5] == mark and board[2] == mark) or  
            (board[9] == mark and board[6] == mark and board[3] == mark) or  
            (board[7] == mark and board[5] == mark and board[3] == mark) or  
            (board[9] == mark and board[5] == mark and board[1] == mark))  


import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('choose your next position (1-9): '))

    return position

def replay():
    return input('do you want to play again? Enter Yes or No: ').lower().startswith('y')


#main code

print('welcome to Tic Tac Toe')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play?Enter yes or no:')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("Player1 has won!")
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print('The match is draw!')
                    break
                else:
                    turn = 'Player2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    if turn == 'Player 1'
                        turn = 'Player 2'
                    else:
                        turn = 'Player 1'
    if not replay():
        break
