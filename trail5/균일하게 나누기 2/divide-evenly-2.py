n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 1. y좌표 기준으로 오름차순 정렬 (수평선을 아래에서 위로 올리기 위함)
points.sort(key=lambda p: p[1])

# x좌표 후보
x_candidates = set(p[0] + 0.5 for p in points)

min_answer = float('inf')

for x in x_candidates:
    
    # 2. 초기 상태: 수평선이 모든 점보다 아래에 있다고 가정
    # 모든 점이 수평선 '위쪽(Top)'에 존재합니다.
    tl = sum(1 for p in points if p[0] < x) # 좌상단(Top-Left) 점 개수
    tr = sum(1 for p in points if p[0] > x) # 우상단(Top-Right) 점 개수
    bl = 0 # 좌하단(Bottom-Left)
    br = 0 # 우하단(Bottom-Right)
    
    # 초기 상태에서의 최댓값 갱신
    min_answer = min(min_answer, max(tl, tr, bl, br))
    
    i = 0
    while i < n:
        current_y = points[i][1]
        
        # 3. 같은 y좌표 선상에 있는 점들을 한 번에 처리합니다.
        while i < n and points[i][1] == current_y:
            # 수평선이 현재 점을 지나가므로, 점이 '위'에서 '아래'로 이동합니다.
            if points[i][0] < x:
                tl -= 1
                bl += 1
            else:
                tr -= 1
                br += 1
            i += 1 # 다음 점으로 이동
            
        # 4. 수평선이 current_y를 완전히 지나간 직후의 상태로 정답을 갱신합니다.
        current_max = max(tl, tr, bl, br)
        min_answer = min(min_answer, current_max)

print(min_answer)

# n = int(input())
# points = [tuple(map(int, input().split())) for _ in range(n)]

# # 1. 탐색할 후보 선분 추출 (점들의 좌표 + 0.5 위치)
# # set을 사용하여 중복된 좌표 위치는 한 번만 탐색하도록 최적화
# x_candidates = set([p[0] + 0.5 for p in points])
# y_candidates = set([p[1] + 0.5 for p in points])

# min_answer = float('inf')

# for x in x_candidates:
#     for y in y_candidates:
        
#         div = [0, 0, 0, 0]

#         for r, c in points:
#             if r < x and c < y:     # 좌하
#                 div[0] += 1
#             elif r > x and c < y:   # 우하
#                 div[1] += 1
#             elif r < x and c > y:   # 좌상
#                 div[2] += 1
#             elif r > x and c > y:   # 우상 
#                 div[3] += 1
        
#         min_answer = min(min_answer, max(div))

# print(min_answer)