import numpy as np
from tool.check_win import get_position, check_win


def check_three(board : list, row : int, col : int, choice : int, player : int) -> int:
    np_board = np.array(board)
    np_board = np_board.reshape(row, col)

    new_board, y = get_position(np_board, choice, player)
    posible_three = 0
    for i in range(7):
        
        if (check_win(new_board, row, col, i, 1)): 
            posible_three += 1

    return posible_three

# test_empty = [[
#     0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0,
#     0, 1, 0, 1, 0, 0, 0,
#     0, 1, 0, 1, 0, 0, 0,
#     0, 1, 1, 1, 0, 0, 0,
#     0, 2, 1, 2, 0, 0, 0,
# ]]
# print(check_three(test_empty, 6, 7, 2, 1))
