n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 시작점들의 최대값이 끝점들의 최소값보다 작거나 같아야한다 O(N)
max_start = max(x1 for x1, _ in segments)
min_end = min(x2 for _, x2 in segments)

print("Yes" if max_start <= min_end else "No")


# 기존방식은 불필요한 반복이 많아짐. O(N * X)
# min_x = min(x1 for x1, _ in segments)
# max_x = max(x2 for _, x2 in segments)

# answer = "No"
# # 확인 할 범위 
# for i in range(min_x, max_x + 1):
#     checked = [False] * n
#     for idx, (x1, x2) in enumerate(segments):
#         if x1 <= i <= x2:
#             checked[idx] = True
    
#     count = 0
#     for c in checked:
#         if c == True:
#             count += 1
    
#     if count == n:
#         answer = "Yes"
#         break

# print(answer)