###############
# крестики нолики
##############


X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruction():
    """Выводит на экран инструкцию для игрока"""
    print(
        """
        Введите число от 0 до 8:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

        \n
        """

    )

def ask_yes_no(question):
    """задает вопрос да или нет"""
    responce = None
    while responce not in ("y", "n"):
        responce = input(question).lower()
    return  responce

def ask_number(question,low,high):
    """просит ввести число из диапазона"""
    responce = None
    while responce not  in range(low,high):
        responce = int(input(question))
    return  responce

def pieces():
    go_first = ask_yes_no("Оставить ход за тобой y/n?")
    if go_first =="y":
        human = X
        computer = O
    else:
        human = O
        computer = X
    return computer,human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_boadr(board):
    print("\n\t",board[0], "|", board[1], "|", board[2])
    print("\t","--------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--------")
    print("\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """создает доступный список ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8,),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]]==board[row[2]] !=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not  in board:
            return TIE
    return None

def human_move(board, human):
    """ход человка"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери 0-8: ", 0, NUM_SQUARES)
        if move not in legal:
            print("Занято, выбери другое:")
    print("Ладно")
    print(move)
    return move

def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,3,5,7)
    print("я выберу номер", end=" ")

    for move in legal_moves(board):
        board[move] == computer

        if winner(board) == computer:
            print(move)
            return  move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return  move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return  move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("три", the_winner, "ряд\n")
    else:
        print("Ничья\n")
    if the_winner ==computer:
        print("Winner computer")
    elif the_winner == human:
        print("Winner human")
    elif the_winner == TIE:
        print(" Ничья")

def main():
    display_instruction()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_boadr(board)

    while not winner(board):
        if turn==human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_boadr(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

main()