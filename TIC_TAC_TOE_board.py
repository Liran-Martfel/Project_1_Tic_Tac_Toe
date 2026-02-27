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
