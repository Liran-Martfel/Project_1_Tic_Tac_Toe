import time

print ('welcome to the game of Tic Tac Toe❌⭕️\nThe game was made by: Liran Martefl\nI Hope you enjoy😇\n')
player_1_name = input('What is the name of the first player? ')
player_2_name = input('What is the name of the second player? ')

def game_rules():
    rules_of_game =  (f'Hello {player_1_name} and {player_2_name} Nice to meet you!😊 the rules of the game are:\n{'*'*40}'
              f'\n1.Two players game: one is X, the other is O.\n{'*'*40}'
              f'\n2.Players take turns placing their mark in an empty square.\n{'*'*40}'
              f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{'*'*40}'
              f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{'*'*40}'
              f'\n5. You need to press the number in order to replace him and pick the spot\n')
    return rules_of_game

def game_options():
    choose:str = (input('You can see the rules of the game by pressing "r", or to start play by pressing "p":\n'))
    choose.lower()
    if choose == 'r':
        print ('loading....')
        time.sleep (1)
        print (rules)
    else:
        pass

def player_pick():
    time.sleep (0.5)
    player_1: str= (input(f'{player_1_name}, please pick your mark:\npress X for X or O for O: '))
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
        print (f'player 1 is: {player_1} player 2 is: {player_2} GOOD LUCK😄')
        return player_1, player_2

rules = game_rules()
game_options()
player_picking = player_pick()

def board():
    game_board: list = [' 1','2','3',
                        ' 4','5','6',
                        ' 7','8','9']
    for row in range(len(game_board)):
        print(game_board[row],end= ' ')
        match row:
            case 2 | 5:
                    print()
                    print ('----+------+----')
            case 8:
                print()
            case _:
                print(' | ',end= ' ')
    return game_board

board_of_game = board()

def pick_spot():
    while player_pick == 'x':
        player_1_action: int = int(input('What is your move? press the number you want to replace: '))
        if player_1_action in board_of_game:
            board_of_game[player_1_action] = '❌'
        else:
            print ('the place is taken🥲')
        break
