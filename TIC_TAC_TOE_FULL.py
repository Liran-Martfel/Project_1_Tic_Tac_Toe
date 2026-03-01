import time

#Welcome message

print ('welcome to the game of Tic Tac Toe❌⭕️\nThe game was made by: Liran Martefl\nI Hope you enjoy😇\n')
player_1_name = input('What is the name of the first player? ')
player_2_name = input('What is the name of the second player? ')


#showing the rules of the game to the players if they choose to

def game_rules():
    rules_of_game =  (f'Hello {player_1_name} and {player_2_name} Nice to meet you!😊 the rules of the game are:\n{'*'*40}'
              f'\n1.Two players game: one is X, the other is O.\n{'*'*40}'
              f'\n2.Players take turns placing their mark in an empty square.\n{'*'*40}'
              f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{'*'*40}'
              f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{'*'*40}'
              f'\n5. You need to press the number in order to replace him and pick the spot\n')
    return rules_of_game

#player's choosing options

def game_options():
    choose:str = (input('You can see the rules of the game by pressing "r", or to start play by pressing "p":\n'))
    choose = choose.lower()
    if choose == 'r':
        print (f'loading....')
        time.sleep (1)
        print (rules)
    else:
        pass

#first player pick up what mark he wants, then continue

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

#putting the board outside the def so that the board won't get reset everytime the players play

game_board: list = [' 1', '2', '3',
                    ' 4', '5', '6',
                    ' 7', '8', '9']

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


pick_spot(player_picking[0])
pick_spot(player_picking[1])

#Makeing the loop for the game so player 1 and player 2 can play for all spots on board

def play_flow():
    player_action = []
    while len(player_action) < 9:
        pick_spot(player_picking[0])
        if winning_by_row(player_picking[0]):
            print (f'{player_1_name} is the winner!')
        elif winning_by_col(player_picking[0]):
            print (f'{player_1_name} is the winner!')
            break
        elif winning_by_diagonal(player_picking[0]):
            print (f'{player_1_name} is the winner!')
            break
        else:
            pass
        player_action.append(player_picking[0])
        if len(player_action) == 9:
            break
        pick_spot(player_picking[1])
        if winning_by_row(player_picking[1]):
            print (f'{player_2_name} is the winner!')
        elif winning_by_col(player_picking[1]):
            print (f'{player_2_name} is the winner!')
            break
        else:
            pass
        player_action.append(player_picking[1])
        if len(player_action) == 9:
            break


def winning_by_row(sign):
    sign_for_winning = [sign,sign,sign]
    if board_of_game [0:3] == sign_for_winning:
        print ('winner!')
        return True

    if board_of_game [3:6] == sign_for_winning:
        print ('winner!')
        return True

    if board_of_game [6::] == sign_for_winning:
        print ('winner!')
        return True
    else:
        return False

winning_by_row(board_of_game)

def winning_by_col(sign):
    sign_for_winning = [sign,sign,sign]
    if board_of_game [0::3] == sign_for_winning:
        print ('winner!')
        return True

    if board_of_game [1::3] == sign_for_winning:
        print ('winner!')
        return True

    if board_of_game [2::3] == sign_for_winning:
        print ('winner!')
        return True
    else:
        return False

winning_by_col(board_of_game)

def winning_by_diagonal(sign):
    sign_for_winning = [sign,sign,sign]
    if board_of_game [0::4] == sign_for_winning or board_of_game [2:7:2] == sign_for_winning:
        print ('winner!')
        return True
    else:
        return False

winning_by_diagonal(board_of_game)
play_flow()