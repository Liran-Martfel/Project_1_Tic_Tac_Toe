import time

# colors for printing
red = '\033[31m'  # for
orange = '\033[38;5;208m'
light_purple = '\033[38;2;179;136;255m'
reset_color = '\033[0m'


def play_game():
    # Welcome message
    print(
        f'{light_purple}welcome to the game of Tic Tac Toe \nThe game was made by: Liran Martefl\nI Hope you enjoy😇\n')
    player_1_name = input(f'{reset_color}What is your name? ')
    player_2_name = None

    # showing the rules of the game to the players if they choose to
    def game_rules():
        rules_of_game = (f'Hello {player_1_name} Nice to meet you!😊 the rules of the game are:\n{'*' * 40}'
                         f'\n1.Two players game: one is X, the other is O.\n{'*' * 40}'
                         f'\n2.Players take turns placing their mark in an empty square.\n{'*' * 40}'
                         f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{'*' * 40}'
                         f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{'*' * 40}'
                         f'\n5. You need to press the number in order to replace him and pick the spot\n')
        return rules_of_game

    # player's choosing options
    def game_options():
        choose: str = (input(
            f'Hey {player_1_name}, Those are your options:\nTo see the rules of the game press "1"\nfor Player vs Player press "2"\nTo exit press "3"\n'))
        choose = choose.lower()
        if choose == '1':
            print(f'{light_purple}loading....{reset_color}')
            time.sleep(1)
            print(rules)
            return '1'
        elif choose == '2':
            return '2'
        else:
            return '3'

    rules = game_rules()
    counter_of_wins = [0, 0]

    # picking marks for the game

    def player_pick():
        player_1: str = (input(f'{player_1_name}, please pick your mark:\npress X for X or O for O: ''\n'))
        player_1 = player_1.lower()
        if player_1 == 'x':
            player_1 = '❌'
            player_2 = '⭕️'
            print(f'{player_1_name} is: {player_1} {player_2_name} is: {player_2}')
            return player_1, player_2
        else:
            player_1 = '⭕️'
            player_2 = '❌'
            print(f'{player_1_name} is: {player_1} {player_2_name} is: {player_2} GOOD LUCK😄')
            return player_1, player_2
    _board_ = [' 1', '2', '3',
               ' 4', '5', '6',
               ' 7', '8', '9']
    # rules of the board of the game
    def board(current_board):
        for row in range(len(current_board)):
            print(current_board[row], end=' ')
            match row:
                case 2 | 5:
                    print()
                    print('----+-----+----')
                case 8:
                    print()
                case _:
                    print(' | ', end=' ')
        return current_board


    # players pick their spot to play :)
    def pick_spot(sign):
        # each player move
        while True:
            choose = input('player, What is your move? press the number you want to replace: ')
            if choose.isdigit():
                player_action = int(choose)
                if 1 <= player_action <= 9:
                    if board_of_game[player_action - 1] != '❌' and board_of_game[player_action - 1] != '⭕️':
                        board_of_game[player_action - 1] = sign
                        board(game_board)
                        return sign
                    else:
                        print('this place is taken🥲')
                        continue
        return player_action

    def play_flow(checking_board,sign):
        # player 1
        while True:
            pick_spot(sign[0])
            check_draw = draw(player_picking)
            if check_draw == 'reset':
                return 'reset'
            elif (winning_by_row(checking_board, sign[0]) or winning_by_col(game_board, sign[0])
                    or winning_by_diagonal(game_board, sign[0])):
                print(f'{player_1_name} is the winner🥳')
                counter_of_wins[0] += 1
                return counter_of_wins
            elif check_draw:
                print('its a draw🤝🏼')
                break
            # player 2
            pick_spot(sign[1])
            check_draw = draw(player_picking)
            if check_draw == 'reset':
                return 'reset'
            elif (winning_by_row(game_board, sign[1]) or winning_by_col(game_board, sign[1])
                    or winning_by_diagonal(game_board, sign[1])):
                print(f'{player_2_name} is the winner🥳')
                counter_of_wins[1] += 1
                return counter_of_wins
            elif check_draw == True:
                print('its a draw🤝🏼')
                break
            # letting the game_flow know that we sent him a reset option, if True, send it out.
            if draw == 'reset':
                return 'reset'

    def winning_by_row(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0:3] == winning_sign or current_board[3:6] == winning_sign or current_board[
            6::] == winning_sign:
            return True
        else:
            return False

    def winning_by_col(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0::3] == winning_sign or current_board[1::3] == winning_sign or current_board[
            2::3] == winning_sign:
            return True
        else:
            return False

    def winning_by_diagonal(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0::4] == winning_sign or current_board[2:7:2] == winning_sign:
            return True
        else:
            return False

    def draw(marks_on_board):
        winning_ways = [
            # row
            board_of_game[0:3], board_of_game[3:6], board_of_game[6:9],
            # col
            board_of_game[0:9:3], board_of_game[1:9:3], board_of_game[2:9:3],
            # diagonal
            board_of_game[0:9:4], board_of_game[2:7:2]]
        cant_win = 0
        # restarting mid game
        for path in winning_ways:
            if marks_on_board[0] in path and marks_on_board[1] in path:
                cant_win += 1
                if cant_win == 6:
                    print('it is close to a tie, would you like to reset?')
                    asking_for_reset = input('(y/n): ')
                    if asking_for_reset == 'y':
                        print('restarting the game....')
                        time.sleep(0.5)
                        for i in range(9):
                            game_board[i] = _board_[i]
                        return 'reset'
                    else:
                        continue
        if cant_win == 8:
            return True
        return False

    # to create a loop so a reset will be possible, and for counting score
    while True:
        choice = game_options()
        if choice == '3':
            print('Thank you for playing, good bye!')
            break
        if choice == '1':
            continue
        elif choice == '2':
            player_2_name = input(f'{player_1_name}, Who is your opponent? ')
            counter_of_wins = [0, 0]
        while True:
            _board_ = [' 1', '2', '3',
                       ' 4', '5', '6',
                       ' 7', '8', '9']
            player_picking = player_pick()
            game_board = _board_.copy()
            board_of_game = board(game_board)
            signs = player_picking
            result = play_flow(game_board,signs)
            if result == 'reset':
                continue
        # printing the final score after each game
            print(f'{orange}the score is:\nplayer 1: {counter_of_wins[0]}\nplayer 2: {counter_of_wins[1]}')
            restart = input(f'Do you want to play again? press (y/n): {reset_color}')
            restart = restart.lower()
            if restart != 'y':
                print(f'Thank you for playing!')
                if counter_of_wins[0] > counter_of_wins[1]:
                    print(f'The winner is: {player_1_name}🎉🥇🎉')
                    break
                elif counter_of_wins[1] == counter_of_wins[0]:
                    print(f'Its a draw! 🤝🏼 good job! ')
                    break
                else:
                    print(f'The winner is: {player_2_name}🎉🥇🎉')
                    break
            else:
                continue


play_game()
