import time

# colors for printing
red = '\033[31m' 
orange = '\033[38;5;208m'
dark_orange = '\033[38;5;166m'
yellow = '\033[93m'
light_purple = '\033[38;2;179;136;255m'
forest_green = '\033[38;2;46;139;87m'
bright_white = '\033[97m'
reset_color = '\033[0m'

def play_game():
    """
    :return: welcome message
    """
# Welcome message
    line = f'{light_purple}{'─' * 54}{reset_color}'
    print(line)
    print(f'{forest_green}    ✨  WELCOME TO THE GAME OF TIC TAC TOE  ✨{reset_color}')
    print(f'{forest_green}    ✨  Crafted with care by: Liran Martfel ✨{reset_color}')
    print(f'{forest_green}               I hope you enjoy😇                      ')
    print(line)
    player_1_name = input(f'{reset_color}What is your name? \n')
    player_2_name = None

# showing the rules of the game to the players if they choose to
    def game_rules():
        """
        :return: prints the rules of the game
        """
        rules_of_game = (f'Hello {player_1_name} Nice to meet you!😊 the rules of the game are:\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n1.Two players game: one is X, the other is O.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n2.Players take turns placing their mark in a numbered square.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n3.First player to get 3 in a row (Row or Column or diagonal) wins.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n4.If there is no way for either player to get three in a row, it is a Tie.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n5.You need to press the number in order to replace it\n{forest_green}{'─' * 60}{reset_color}')
        return rules_of_game

# player's choosing options
    def game_options():
        """
        showing the menu of the game
        :return: hte choice of the player for the game
        """
        choose: str = (input(f'Hey {player_1_name}, Those are your options:\nTo see the rules of the game press {light_purple}"1"{reset_color}\n'
                       f'for Player vs Player press {light_purple}"2"{reset_color}\nTo exit press {light_purple}"3"{reset_color}\n'))
        choose = choose.lower()
        if choose == '1':
            print(f'{forest_green}loading....{reset_color}')
            time.sleep(1)
            print(rules)
            return '1'
        elif choose == '2':
            return '2'
        else:
            return '3'
    rules = game_rules()
    counter_of_wins = [0, 0]
    tie_counter = [0]

    def player_pick():
        """
        player picks his mark for the game
        :return: the marks
        """
        player_1: str = (input(f'{player_1_name}, please pick your mark:\npress X for {forest_green}X{reset_color} or anything else for {red}O{reset_color}: ''\n'))
        player_1 = player_1.lower()
        if player_1 == 'x':
            player_1 = 'X'
            player_2 = 'O'
            print(f'\n{player_1_name} is:{player_1}\n{player_2_name} is:{player_2}\nGOOD LUCK😄\n')
            return player_1, player_2
        else:
            player_1 = 'O'
            player_2 = 'X'
            print(f'\n{player_1_name} is:{player_1}\n{player_2_name} is:{player_2}\nGOOD LUCK😄\n')
            return player_1, player_2
    _board_ = [' 1', '2', '3',
               ' 4', '5', '6',
               ' 7', '8', '9']
# rules of the board of the game
    def board(current_board):
        """
        :param current_board: the board itself at this moment
        :return: the board of the current game that is running
        """
        def c(mark):
            mark_str = str(mark).strip()
            if 'X' in mark_str:
                return f"{forest_green}X{reset_color}"
            elif 'O' in mark_str:
                return f"{red}O{reset_color}"
            return mark_str
        print(f" {c(current_board[0])} | {c(current_board[1])} | {c(current_board[2])} ")
        print("---+---+---")
        print(f" {c(current_board[3])} | {c(current_board[4])} | {c(current_board[5])} ")
        print("---+---+---")
        print(f" {c(current_board[6])} | {c(current_board[7])} | {c(current_board[8])} ")

        return current_board

# players pick their spot to play :)
    def pick_spot(sign):
        """
        :param sign: sign is the mark that the player choose, then seeing if the [i] in the board is available, and if so, replace it with the mark
        :return: the action of the player, and print if the place is taken
        """
        # each player move
        while True:
            choose = input('\nplayer, What is your move? press the number you want to replace: ')
            if choose.isdigit():
                player_action = int(choose)
                if 1 <= player_action <= 9:
                    if board_of_game[player_action - 1] != 'X' and board_of_game[player_action - 1] != 'O':
                        board_of_game[player_action - 1] = sign
                        board(game_board)
                        return sign
                    else:
                        print('this place is taken🥲')
                        continue
                        
    def play_flow(current_board, sign):
        """
        this def is the heart of the game, where all the def come together.
        :param current_board: the board of the game at this point of the game
        :param sign: the mark that the player
        :return: returning 'reset' if the player choose to reset the game
        """
        for turn in range (9):
            if turn % 2 == 0:
                name = player_1_name
                mark = sign[0]
                i = 0
            else:
                name = player_2_name
                mark = sign[1]
                i = 1
            pick_spot(mark)
            if winning_by_row_col_diagonal(current_board, mark):
                print(f'\n{yellow}-----{name} is the winner🥳-----{reset_color}\n')
                counter_of_wins[i] += 1
                return counter_of_wins
            check_draw = draw(sign,current_board)
            if check_draw == 'reset':
                return 'reset'
            elif check_draw == True:
                print('its a draw🤝🏼')
                tie_counter[0] += 1
                return tie_counter
# letting the game_flow know that we sent him a reset option, if True, send it out.
            if draw == 'reset':
                return 'reset'
        return counter_of_wins,tie_counter

    def winning_by_row_col_diagonal(current_board, sign):
        """
        this def is showing how you can win, win 3 sign the same in a row.
        :param current_board: checking with the board
        :param sign: getting inside a list
        :return:True or False
        """
        winning_sign = [sign, sign, sign]
        if winning_sign in path_for_win(current_board):
            return True
        else:
            return False
#bool check if any cross-path is True, then return it to the board and checking with winning def if True or False
    def path_for_win(current_board):
        """
        :param current_board: showing all the possibilities you can win with in the board
        :return: all the option for winning
        """
        return [
                current_board[0:3], current_board[3:6], current_board[6::], #row
                current_board[0::3], current_board[1::3], current_board[2::3], #col
                current_board[0::4], current_board[2:7:2] # diagonal
                ]

    def draw(marks_on_board,current_board):
        """
        this def responsibility is to check if the player is close to a tie, and ask if he wants to reset, if he does, print the board from scratch and reset the game
        :param marks_on_board: where the player placed their mark on the board
        :param current_board: checking the board for tie or reset
        :return:
        """
        cant_win = 0
# restarting mid game
        for path in path_for_win(current_board):
            if marks_on_board[0] in path and marks_on_board[1] in path:
                cant_win += 1
                if cant_win == 6:
                    print(f'{dark_orange}it is close to a tie, would you like to reset?')
                    asking_for_reset = input(f'(y/n): {reset_color}')
                    if asking_for_reset == 'y':
                        print('restarting the game....')
                        time.sleep(1)
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
            print('Thank you for playing, goodbye!')
            break
        if choice == '1':
            continue
        elif choice == '2':
            player_2_name = input(f'{player_1_name}, {light_purple}Who is your opponent?{reset_color} ')
            counter_of_wins = [0, 0]
            tie_counter = [0]
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
            print(f'{orange}the score is:\n{player_1_name}: {bright_white}{counter_of_wins[0]}{orange}'
                  f'\n{player_2_name}: {bright_white}{counter_of_wins[1]}{orange}\nDraws: {bright_white}{tie_counter[0]}')
            restart = input(f'Do you want to play again?\n(y/n): {reset_color}')
            restart = restart.lower()
            if restart != 'y':
                if counter_of_wins[0] > counter_of_wins[1]:
                    print(f'\n{yellow}The winner is: {player_1_name}🎉🥇🎉{reset_color}\n')
                    print(f'{light_purple}Thank you for playing!{reset_color}\n')
                    break
                elif (tie_counter[0] > counter_of_wins[1] and tie_counter[0] > counter_of_wins[0]) or (counter_of_wins[0] == counter_of_wins[1]):
                    print(f'\n{bright_white}Its a draw! 🤝🏼 good job!{reset_color}\n')
                    print(f'{light_purple}Thank you for playing!{reset_color}\n')
                    break
                else:
                    print(f'\n{yellow}The winner is: {player_2_name}🎉🥇🎉{reset_color}\n')
                    print(f'{light_purple}Thank you for playing!{reset_color}\n')
                    break
            else:
                continue
play_game()
