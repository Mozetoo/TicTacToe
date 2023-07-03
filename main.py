board = [' ' for _ in range(9)]


def display_board():
    print('-------------------')
    print(' | ', board[0], ' | ', board[1], ' | ', board[2], ' | ')
    print('-------------------')
    print(' | ', board[3], '| ', board[4], ' | ', board[5], ' | ')
    print('-------------------')
    print(' | ', board[6], ' | ', board[7], ' | ', board[8], ' | ')
    print('-------------------')


def is_game_over():
    global winner
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == "X" != ' ':
            winner = 'X'
            return True
        elif board[i] == board[i + 1] == board[i + 2] == "O" != ' ':
            winner = 'O'
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == "X" != ' ':
            winner = 'X'
            return True
        elif board[i] == board[i + 3] == board[i + 6] == "O" != ' ':
            winner = 'O'
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == 'X' != ' ':
        winner = 'X'
        return True
    elif board[0] == board[4] == board[8] == 'O' != ' ':
        winner = 'O'
        return True
    if board[2] == board[4] == board[6] == "X" != ' ':
        winner = 'X'
        return True
    elif board[2] == board[4] == board[6] == "O" != ' ':
        winner = 'O'
        return True
    # Check if the board is full
    if ' ' not in board:
        return True
    return False


def final_check():
    global winner
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == "X" != ' ':
            winner = 'X'
            return True
        elif board[i] == board[i + 1] == board[i + 2] == "O" != ' ':
            winner = 'O'
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == "X" != ' ':
            winner = 'X'
            return True
        elif board[i] == board[i + 3] == board[i + 6] == "O" != ' ':
            winner = 'O'
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == 'X' != ' ':
        winner = 'X'
        return True
    elif board[0] == board[4] == board[8] == 'O' != ' ':
        winner = 'O'
        return True
    if board[2] == board[4] == board[6] == "X" != ' ':
        winner = 'X'
        return True
    elif board[2] == board[4] == board[6] == "O" != ' ':
        winner = 'O'
        return True
    return False


def tic_tac_toe():
    user_input = input("Choose X or O: ").upper()
    if user_input == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    print(f"You are {user_input}\nOpponent is {opponent}")

    while not is_game_over() and ' ' in board:
        display_board()
        print("Your Turn")
        user_choice = int(input("Choose Placement from (0 - 8): "))
        if board[user_choice] == ' ':
            board[user_choice] = user_input
        display_board()

        if not is_game_over() and ' ' in board:
            print("Rival Turn")
            opp_choice = int(input("Choose Placement from (0 - 8): "))
            if board[opp_choice] == ' ':
                board[opp_choice] = opponent
            display_board()
    if final_check():
        print("Player", winner, "wins!")
    else:
        print("It's a tie!")


tic_tac_toe()