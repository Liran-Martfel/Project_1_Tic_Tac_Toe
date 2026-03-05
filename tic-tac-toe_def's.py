#putting the board outside of the def so that the board won't get reset everytime the players play

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
            player_action: int = int(input('player, What is your move? press the number you want to replace: '))
            if board_of_game[player_action - 1] != '❌' and board_of_game[player_action - 1] != '⭕️':
                board_of_game[player_action - 1] = sign
                board()
                break
            else:
                print ('the place is taken🥲')
                continue

pick_spot(player_picking[0])
pick_spot(player_picking[1])
