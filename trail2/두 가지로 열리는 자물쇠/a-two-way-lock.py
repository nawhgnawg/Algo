n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# 원형 다이얼에서 두 숫자의 거리가 2 이하인지 확인하는 함수
def is_close(u, v):
    diff = abs(u - v)
    # 직선 거리와 원형으로 반대로 돌아가는 거리 중 최솟값
    return min(diff, n - diff) <= 2

# 세 자리가 모두 해당 조합과 가까운지 검사
def is_match(x, y, z, target_a, target_b, target_c):
    return is_close(x, target_a) and is_close(y, target_b) and is_close(z, target_c)


answer = 0

# 1부터 n까지 3개의 다이얼을 모두 돌려봅니다.
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            # 첫 번째 조합과 모두 가깝거나, 두 번째 조합과 모두 가까우면 카운트
            if is_match(x, y, z, a1, b1, c1) or is_match(x, y, z, a2, b2, c2):
                answer += 1

print(answer)