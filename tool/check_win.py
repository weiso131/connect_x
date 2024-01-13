import numpy as np


def get_position(board : np.array, choice : int, player : int) -> np.array:
    new_board = board.copy()
    for i in range(5, -1, -1):
        if (board[i][choice] == 0): 
            new_board[i][choice] = player
            return new_board, i
    return board, 5

def dfs(board : np.array, y : int, x : int, dy : int, dx : int, player : int, count=0) -> int:
    rows = len(board)
    cols = len(board[0])
    if ((y >= 0 and y < rows and x >= 0 and x < cols) == False):
        return count
    if (board[y, x] != player):
        return count
    return dfs(board, y + dy, x + dx, dy, dx, player, count + 1)


def check_win(board : list, row : int, col : int, choice : int, player : int) -> bool:
    np_board = np.array(board)
    np_board = np_board.reshape(row, col)

    x = choice
    new_board, y = get_position(np_board, choice, player)
    
    derivative = [(1, 1), (-1, 1), (1, 0), (0, 1)]
    for i, j in derivative:
        count = dfs(new_board, y, x, i, j, player) + dfs(new_board, y, x, -i, -j, player) -1
        if (count >= 4):
            return True
    return False









test_empty = [[
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
]]
test_12 = [[
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0,
    0, 0, 2, 2, 0, 0, 0,
    1, 1, 2, 2, 0, 0, 0,
]]
print(check_win(test_12, 6, 7, 1, 1))
print(check_win(test_12, 6, 7, 0, 1))