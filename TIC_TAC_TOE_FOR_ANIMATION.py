def path_for_win(current_board):
    return [
        current_board[0:3], current_board[3:6], current_board[6::],
        current_board[0::3], current_board[1::3], current_board[2::3],
        current_board[0::4], current_board[2:7:2]
    ]
def winning_by_row_col_diagonal(current_board, mark):
    winning_sign = [mark, mark, mark]
    return winning_sign in path_for_win(current_board)

def draw(marks_on_board, current_board):
    cant_win = 0
    for path in path_for_win(current_board):
        if marks_on_board[0] in path and marks_on_board[1] in path:
            cant_win += 1
    if cant_win == 8:
        return True
    return False


def play_game():
    pass

if __name__ == "__main__":
    play_game()