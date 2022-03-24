'''
Lex King
lab9.py
this code is a lets the user play tic tac toe.
this is my code
'''

def build_board():
    board = []
    for i in range(1, 10):
        board.append(i)
    return board

def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def fill_spot(board, position, character):
    if character == "x" or "o":
        board[position -1] = character


def is_legal(board, position):
    if position in board and board[position -1] == position:
        return True

def winning_game(board, character):
    for i in range(3):
        number = 3 * i
        if board[number] != character:
            continue
        if board[number + 1] != character:
            continue
        if board[number + 2] != character:
            continue
        return True
    for i in range(3):
        if board[i] != character:
            continue
        if board[i + 3] != character:
            continue
        if board[i + 6] != character:
            continue
        return True
    if board[2] == character:
        if board[4] == character:
            if board[6] == character:
                return True
    if board[0] == character:
        if board[4] == character:
            if board[8] == character:
                return True


def game_over(board):
    if winning_game(board, "x") is True or winning_game(board, 'o') is True:
        return True
    else:
        for i in range(1, 10):
            if board[i - 1] == i:
                return False
        return True

def play():
    board = build_board()
    print_board(board)
    player1 = 'x'
    print("Player one is X!")
    player2 = "o"
    print("Player two is O!")
    while True:
        if game_over(board) is True:
            break
        else:
            position = int(input("Player one enter position to play: "))
            if is_legal(board, position) is True:
                fill_spot(board, position, player1)
            print_board(board)
            if game_over(board) is True:
                break
            else:
                position = int(input("Player two enter position to play: "))
                if is_legal(board, position) is True:
                    fill_spot(board, position, player2)
                print_board(board)
    if winning_game(board, player1) is True:
        print("Player one wins!")
    elif winning_game(board,player2) is True:
        print("Player two wins!")
    else:
        print("It is a tie!")

def main():
    pass



if __name__ == '__main__':
    main()
