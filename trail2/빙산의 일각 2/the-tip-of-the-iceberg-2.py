n = int(input())
h = [int(input()) for _ in range(n)]

max_chunks = 0

# 해수면 높이 s는 0부터 max(h) - 1까지 탐색
for s in range(max(h)):
    # 💡 덩어리의 '시작점'만 골라 카운트 (플래그, 새 배열 불필요)
    chunks = 0
    for i in range(n):
        if h[i] > s and (i == 0 or h[i - 1] <= s):
            chunks += 1
    max_chunks = max(max_chunks, chunks)

print(max_chunks)
            

# max_area = 0

# for s in range(max(h)):
#     area = 0
#     is_new = False
#     new_h = [c - s for c in h]
#     for curr_h in new_h:
#         if curr_h > 0:
#             # 새로운 덩어리라면
#             if is_new == False:
#                 area += 1
#                 is_new = True
#         else:
#             is_new = False
    
#     max_area = max(area, max_area)

# print(max_area)