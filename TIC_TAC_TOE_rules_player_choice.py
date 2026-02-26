#mission to success:
#1. ask the player if he would like to be an X or an O✅.
#1.1 show players what they are (X or O)✅
#1.2 make the rules✅
#1.3 make an option to show the rules✅
#2. show the board - 3 by 3.
#3. each player pick a spot
#3.1 checking for illegal moves.
#3.2 having a delay of 0.5 till showing the new board with the pick.
#3.3 in case of a draw, keep the option to reset or quit the game.
#4. checking for a winner. if there is. print it nicely.
#4.1 make a score board.
import time

print ('welcome to the game of Tic Tac Toe❌⭕️\nThe game was made by: Liran Martefl\nI Hope you enjoy😇\n')
player_1_name = input('What is the name of the first player? ')
player_2_name = input('What is the name of the second player? ')

def game_rules():
    rules_of_game =  (f'Hello {player_1_name} and {player_2_name} Nice to meet you!😊 the rules of the game are:\n{'*'*40}'
              f'\n1.Two players game: one is X, the other is O.\n{'*'*40}'
              f'\n2.Players take turns placing their mark in an empty square.\n{'*'*40}'
              f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{'*'*40}'
              f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{'*'*40}\n')
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
        print (f'player 1 is: {player_1} player 2 is: {player_2}')
        return player_1, player_2

rules = game_rules()
game_options()
player_picking = player_pick()


