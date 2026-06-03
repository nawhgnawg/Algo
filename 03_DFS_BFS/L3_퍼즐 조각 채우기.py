# 프로그래머스 level 3 - 퍼즐 조각 채우기
# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque

def extract_pieces(board, target_value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    pieces = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == target_value and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True

                # 현재 퍼즐 조각의 좌표들을 담을 리스트
                piece = [(i, j)]

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == target_value and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                piece.append((nx, ny))

                pieces.append(piece)

    return pieces


def normalize(piece):
    min_x = min(p[0] for p in piece)
    min_y = min(p[1] for p in piece)
    return sorted([(p[0] - min_x, p[1] - min_y) for p in piece])


def rotate(piece):
    rotated = [(p[1], -p[0]) for p in piece]
    return normalize(rotated)


def solution(game_board, table):
    # 1. 빈칸(0)과 퍼즐(1) 추출 후 모두 영점 조절(정규화)
    empty_spaces = [normalize(p) for p in extract_pieces(game_board, 0)]
    puzzles = [normalize(p) for p in extract_pieces(table, 1)]

    answer = 0
    used_puzzles = [False] * len(puzzles)  # 퍼즐 사용 여부 체크

    # 2. 빈칸을 하나씩 꺼내서 퍼즐을 맞춰봄
    for space in empty_spaces:
        for i, puzzle in enumerate(puzzles):
            if used_puzzles[i]:  # 이미 사용한 퍼즐은 패스
                continue

            # 칸 수가 다르면 애초에 모양이 맞을 수 없으므로 패스 (최적화)
            if len(space) != len(puzzle):
                continue

            matched = False
            current_puzzle = puzzle

            # 3. 0도, 90도, 180도, 270도 돌려가며 비교
            for _ in range(4):
                if space == current_puzzle:  # 모양이 완벽히 일치하면!
                    matched = True
                    break
                current_puzzle = rotate(current_puzzle)  # 안 맞으면 90도 회전

            # 4. 맞췄다면 정답 처리 후 다음 빈칸으로 넘어감
            if matched:
                used_puzzles[i] = True
                answer += len(space)  # 채운 칸 수만큼 더하기
                break

    return answer