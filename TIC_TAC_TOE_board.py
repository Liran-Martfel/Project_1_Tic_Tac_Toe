#import TIC_TAC_TOE_rules_player_choice

#def board():
game_board: list = [' 1',' 2',' 3',
                    ' 4',' 5',' 6',
                    ' 7',' 8',' 9']
for row in range(len(game_board)):
    match row:
        case 0:
            game_board[row] = ' 1'
        case 1:
            game_board[row] = ' 2'
        case 2:
            game_board[row] = ' 3'
        case 3:
            print()
            print ('----+-----+-----')
            game_board[row] = ' 4'
        case 4:
            game_board[row] = ' 5'
        case 5:
            game_board[row] = ' 6'
        case 6:
            print()
            print ('----+-----+-----')
            game_board[row] = ' 7'
        case 7:
            game_board[row] = ' 8'
        case 8:
            game_board[row] = ' 9'
    print(game_board[row],end ='  | ')
