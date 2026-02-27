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
                        break
                    else:
                        print ('the place is taken🥲')
                        continue
        return player_action

pick_spot(player_picking[0])
pick_spot(player_picking[1])

#Makeing the loop for the game so player 1 and player 2 can play for all spots on board

def play_flow():
    player_action = []
    while len(player_action) < 9:
        pick_spot(player_picking[0])
        player_action.append(player_picking[0])
        if len(player_action) == 9:
            break
        pick_spot(player_picking[1])
        player_action.append(player_picking[1])
        if len(player_action) == 9:
            break

play_flow()
