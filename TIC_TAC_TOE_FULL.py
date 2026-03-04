import time

#colors for printing
red = '\033[31m' # for
orange = '\033[38;5;208m'
light_purple = '\033[38;2;179;136;255m'
reset_color = '\033[0m'

#Welcome message
print (f'{light_purple}welcome to the game of Tic Tac Toe \nThe game was made by: Liran Martefl\nI Hope you enjoy😇\n')
player_1_name = input(f'{reset_color}What is your name? ')
player_2_name = None
#showing the rules of the game to the players if they choose to

def game_rules():
    rules_of_game =  (f'Hello {player_1_name} Nice to meet you!😊 the rules of the game are:\n{'*'*40}'
              f'\n1.Two players game: one is X, the other is O.\n{'*'*40}'
              f'\n2.Players take turns placing their mark in an empty square.\n{'*'*40}'
              f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{'*'*40}'
              f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{'*'*40}'
              f'\n5. You need to press the number in order to replace him and pick the spot\n')
    return rules_of_game

#player's choosing options

def game_options():
    choose:str = (input(f'Hey {player_1_name}, Those are your options:\nTo see the rules of the game press "1"\nfor Player vs Player press "2"\nTo exit press "3"\n'))
    choose = choose.lower()
    if choose == '1':
        print (f'{light_purple}loading....{reset_color}')
        time.sleep (1)
        print (rules)
        return '1'
    elif choose == '2':
        return '2'
    else:
        return '3'
_board_ = [' 1', '2', '3',
           ' 4', '5', '6',
           ' 7', '8', '9']
rules = game_rules()
counter_of_wins = [0,0]
while True:
    game_board = _board_.copy()
    choice = game_options()
    if choice == '3':
        print ('Thank you for playing, good bye!')
        break
    if choice == '1':
        continue
    elif choice == '2':
        player_2_name = input(f'{player_1_name}, Who is your opponent? ')
        counter_of_wins = [0, 0]
        # clean board for reset
        _board_ = [' 1', '2', '3',
                   ' 4', '5', '6',
                   ' 7', '8', '9']
    while True:
        game_board = _board_.copy()
        def player_pick():
            time.sleep (0.5)
            player_1: str= (input(f'{player_1_name}, please pick your mark:\npress X for X or O for O: ''\n'))
            player_1.lower()
            if player_1 == 'x':
                player_1 = '❌'
                player_2 = '⭕️'
                time.sleep (0.5)
                print (f'{player_1_name} is: {player_1} {player_2_name} is: {player_2}')
                return player_1, player_2
            else:
                player_1 = '⭕️'
                player_2 = '❌'
                time.sleep (0.5)
                print (f'{player_1_name} is: {player_1} {player_2_name} is: {player_2} GOOD LUCK😄')
                return player_1, player_2
        player_picking = player_pick()

        #putting the board outside the def so that the board won't get reset everytime the players play

        #rules of the board print

        def board():
            for row in range(len(game_board)):
                print(game_board[row],end= ' ')
                match row:
                    case 2 | 5:
                            print()
                            print ('----+-----+----')
                    case 8:
                        print()
                    case _:
                        print(' | ',end= ' ')
            return game_board
        board_of_game = board()


        #players pick their spot to play :)

        def pick_spot(sign):
                #each player move
                while True:
                    time.sleep (0.5)
                    choose = input('player, What is your move? press the number you want to replace: ')
                    if choose.isdigit():
                        player_action = int(choose)
                        if 1 <= player_action <= 9:
                            if board_of_game[player_action - 1] != '❌' and board_of_game[player_action - 1] != '⭕️':
                                board_of_game[player_action - 1] = sign
                                board()
                                return sign
                            else:
                                print ('this place is taken🥲')
                                continue
                return player_action


        #Makeing the loop for the game so player 1 and player 2 can play for all spots on board

        def play_flow():
        #player 1
            while True:
                pick_spot(player_picking[0])
                if winning_by_row(player_picking[0]) or winning_by_col(player_picking[0]) or winning_by_diagonal(player_picking[0]):
                    print (f'{player_1_name} is the winner🥳')
                    counter_of_wins[0] += 1
                    return counter_of_wins
                elif draw():
                    print ('its a draw🤝🏼')
                    break
        # player 2
                pick_spot(player_picking[1])
                if winning_by_row(player_picking[1]) or winning_by_col(player_picking[1]) or winning_by_diagonal(player_picking[1]):
                    print (f'{player_2_name} is the winner🥳')
                    counter_of_wins[1] += 1
                    return counter_of_wins
                elif draw():
                    print('its a draw🤝🏼')
                    break

                #letting the game_flow know that we sent him a reset option, if True, send it out.
                if_reset = draw
                if if_reset == 'reset':
                    return 'reset'


        def winning_by_row(sign):
            sign_for_winning = [sign,sign,sign]
            if board_of_game [0:3] == sign_for_winning or board_of_game [3:6] == sign_for_winning or board_of_game [6::] == sign_for_winning:
                return True
            else:
                return False
        winning_by_row(board_of_game)

        def winning_by_col(sign):
            sign_for_winning = [sign,sign,sign]
            if board_of_game [0::3] == sign_for_winning or board_of_game [1::3] == sign_for_winning or board_of_game [2::3] == sign_for_winning:
                return True
            else:
                return False
        winning_by_col(board_of_game)

        def winning_by_diagonal(sign):
            winning_sign = [sign,sign,sign]
            if board_of_game [0::4] == winning_sign or board_of_game [2:7:2] == winning_sign:
                return True
            else:
                return False
        winning_by_diagonal(board_of_game)

    #draw play and reset mid_game
        def draw():
            winning_ways = [
                #row
                board_of_game[0:3], board_of_game[3:6], board_of_game[6:9],
                #col
                board_of_game[0:9:3], board_of_game[1:9:3], board_of_game[2:9:3],
                #diagonal
                board_of_game[0:9:4], board_of_game[2:7:2]]
            cant_win = 0
            for path in winning_ways:
                if player_picking[0] in path and player_picking[1] in path:
                    cant_win += 1

                #reset_mid_game
            if cant_win == 8:
                return True
            elif cant_win >= 6:
                asking_for_reset = input('would you like to reset the game? (y/n): ')
                if asking_for_reset == 'y':
                    print ('restarting the game....')
                    time.sleep(0.5)
                    for i in range(9):
                        game_board[i] = _board_[i]
                    board()
                    #returning reset for game_flow
                    return 'reset'
                else:
                    return False
            else:
                return False

        #checking if game_flow returned reset, if it did, we continue like nothing happened
        if play_flow() == 'reset':
            continue

        print (f'{orange}the score is:\nplayer 1: {counter_of_wins[0]}\nplayer 2: {counter_of_wins[1]}')
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