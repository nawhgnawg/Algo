# 프로그래머스 - 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694


rectangle = [[1, 1, 7, 4],
             [3, 2, 5, 5],
             [4, 3, 6, 9],
             [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
dap = 17

def solution(rectangle, characterX, characterY, itemX, itemY):

    def check(current, rectangle):
        result = []
        point_x, point_y = current
        # 어디 변인지 체크
        for i in range(len(rectangle)):
            x1, y1, x2, y2 = rectangle[i]
            if y1 == point_y and x1 <= point_x < x2:    # 밑변
                result.append(0)
            if x2 == point_x and y1 <= point_y < y2:    # 우변
                result.append(1)
            if y2 == point_y and x1 < point_x <= x2:    # 윗변
                result.append(2)
            if x1 == point_x and y1 < point_y <= y2:    # 좌변
                result.append(3)

        # l_index 를 만들어 return
        # 교점일 경우 len(result) == 2
        # l_index 에 우선순위 존재 0 -> 3 -> 2 -> 1 -> 0 -> ,,,
        return max(result) if set(result) == {0, 3} else min(result)

    def move(point, l_index):
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dx, dy = direct[l_index]
        x, y = point
        return x + dx, y + dy

    start = (characterX, characterY)
    item = (itemX, itemY)
    current = start
    start_d, item_d = 0, 0
    while True:
        l_index = check(current, rectangle)
        current = move(current, l_index)
        start_d += 1
        if current == item:
            item_d = start_d
        if current == start:
            break

    return min(start_d - item_d, item_d)

# 1,3 -> check 실행 -> return [3] -> move 실행 -> 밑으로 한칸 이동, current = 1, 2 -> 거리 1 추가 -> check 실행
# -> return [
print(solution(rectangle, characterX, characterY, itemX, itemY).__eq__(17))
