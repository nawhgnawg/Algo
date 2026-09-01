n = int(input())
a, b, c = map(int, input().split())

# x와 거리가 2 이하인 숫자의 개수 구하기
def get_match_count(target):
    start = max(1, target - 2)
    end = min(n, target + 2)
    return end - start + 1

# 각 자리에서 거리가 2보다 큰(조건을 만족하지 않는) 숫자의 개수
fail_a = n - get_match_count(a)
fail_b = n - get_match_count(b)
fail_c = n - get_match_count(c)

# 전체 조합(N^3)에서 세 자리 모두 실패하는 조합의 수를 뺌 (O(1))
answer = (n ** 3) - (fail_a * fail_b * fail_c)

print(answer)


# answer = 0

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             # 입력한 번호 (x, y, z)
#             x, y, z = i + 1, j + 1, k + 1

#             if abs(x - a) <= 2 or abs(y - b) <= 2 or abs(z - c) <= 2:
#                 answer += 1

# print(answer)