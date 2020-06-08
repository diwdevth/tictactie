from os import system
import time
from math import inf as infinity
lengths = 12
board = ['_' for x in range(lengths)]

def printBoard(board):
    print("", board[0], "|", board[1], "|", board[2], "|" , board[3], "|" , board[4], " ")
    print("-------------------")
    print("", board[5], "|", board[6], "|", board[7], "|" , board[8], "|" , board[9], " ")
    # print("-------------------")
    # print("", board[10], "|", board[11], "|", board[12], "|" , board[13], "|" , board[14], " ")
    # print("-------------------")
    # print("", board[15], "|", board[16], "|", board[17], "|" , board[18], "|" , board[19], " ")
    # print("-------------------")
    # print("", board[20], "|", board[21], "|", board[22], "|" , board[23], "|" , board[24], " ")


def evaluate(state):
    if winner(state, "O"):
        score = +1
    elif winner(state, "X"):
        score = -1
    else:
        score = 0
    return score

def availspots(board):
    result = []
    #enumerate() แจกแจงค่า index กับ value ใช้ได้กับ list
    for i, j in enumerate(board):
        if j == '_':
            result.append(i)
    return result

def winner(state, player):
    win_state = [
        [state[0], state[1],state[2]],
        [state[3], state[4],state[5]],
        [state[6], state[7],state[8]],
        [state[0], state[3],state[6]],
        [state[1], state[4],state[7]],
        [state[2], state[5],state[8]],
        [state[0], state[4],state[8]],
        [state[2], state[4],state[6]]
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    return winner(state, 'X') or winner(state, 'O')

def minimax(board, depth, player):
    if player == 'O':
        best = [-1, -infinity]
    else:
        best = [-1, infinity]

    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, score]
    
    for cell in availspots(board):
        board[cell] = player

        if player == 'O':
            score = minimax(board, depth - 1, 'X')
        else:
            score = minimax(board, depth - 1, 'O')

        board[cell] = '_'
        score[0] = cell
        if player == 'O':
            if best[1] < score[1]:
                best = score
        else:
            if best[1] > score[1]:
                best = score
    # print('best: ',best)
    return best

def human_turn(board):
    depth = len(availspots(board))
    if depth == 0 or game_over(board):
        return 

    move = -1

    while move < 1 or move > 25:
        clean()
        print('Human turn \n')
        printBoard(board)
        move = int(input('Enter position (1..9): '))

        if move <= 25 and move >= 1:
            if board[move-1] == '_':
                move -= 1
                board[move] = 'X'
                printBoard(board)
                return
            else:
                print('Thins positions is not free')
                move = -1
                time.sleep(1)
        else:
            print('bad move')
            move = -1

def clean():
    # i = 1
    system('cls')

def AI_Move():
    depth = len(availspots(board))

    if depth == 0 or game_over(board):
        return 
    
    clean()
    
    print('AI turn \n')
    move = minimax(board, depth, 'O')
    # print('minimax: ',move) [position, 0]
    board[move[0]] = 'O'
    printBoard(board)
    time.sleep(1)

def main(board):
    while len(availspots(board)) > 0 and not game_over(board):
        human_turn(board)
        AI_Move()

    if winner(board, 'X'):
        print('Human win!')
        return 0
    elif winner(board, 'O'):
        print('AI win!')
        return 0
    else:
        print('Draw')
        return 0

if __name__ == '__main__':
    while True:
        main(board)
        board = ['_' for x in range(lengths)]
        again = input('Wanna player again? [y/n]: ')
        if again == 'n':
            break