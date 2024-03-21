# 프로그래머스 - 혼자서 하는 틱택토
# https://school.programmers.co.kr/learn/courses/30/lessons/160585

board = ["O.X", ".O.", "..X"]


# 1차
# 나올 수 없는 조건 -> 1. 'X'가 'O'의 수보다 많거나 'O'가 3개가 연속되었을 때는 같은것도 포함
#                  2. 1개만 작성했을 때 'X'만 있을 때
# 끝나는 조건 구하기 -> 'O' or 'X'가 3개가 가로,세로,대각선으로 있을 때
def check_win(board, t):
    # 가로줄 판단
    for row in board:
        if row == [t, t, t]:
            return True

    # 세로줄 판단
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True

    # 대각선 판단
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [t, t, t]:
        return True

    return False

def solution1(board):
    board = [list(row) for row in board]

    # O의 개수가 X의 개수보다 같거나 1 많아야 함
    o_count, x_count = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                o_count += 1
            if c == 'X':
                x_count += 1

    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    # O 혹은 X만 승리조건을 만족해야함
    if check_win(board, 'O') and check_win(board, 'X'):
        return 0

    # O가 승리했다면 o_count == x_count + 1이여야 함
    if check_win(board, 'O') and o_count != x_count + 1:
        return 0

    # X가 승리했다면 x_count == o_count이여야함
    if check_win(board, 'X') and o_count != x_count:
        return 0

    return 1

print(solution1(board))