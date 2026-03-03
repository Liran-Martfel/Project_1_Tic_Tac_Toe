import time
import random

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
    choose:str = (input('To see the rules of the game press "1"\nfor Player vs Player press "2"\nfor Player vs Computer press "3"\n'))
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
