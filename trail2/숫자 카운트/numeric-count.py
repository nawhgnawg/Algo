n = int(input())

queries = []

for _ in range(n):
    num_str, c1, c2 = input().split()
    # 비교하기 편하게 각 자릿수를 정수 리스트로 변환해 저장
    queries.append(([int(digit) for digit in num_str], int(c1), int(c2)))

answer = 0

# 1. 서로 다른 세 자리 숫자 (i, j, k)를 모두 만들어 봅니다. (504가지)
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # 세 숫자가 모두 달라야 하므로 중복은 패스
            if i == j or j == k or i == k:
                continue

            candidate = [i, j, k]
            is_valid = True

            # 2. 현재 후보 숫자가 B의 모든 질문 조건과 일치하는지 검사
            for query_digits, target_c1, target_c2 in queries:
                strike = 0
                ball = 0

                for idx in range(3):
                    # 위치와 숫자가 모두 같으면 스트라이크 (1번 카운트)
                    if candidate[idx] == query_digits[idx]:
                        strike += 1
                    # 숫자는 포함되어 있지만 위치가 다르면 볼 (2번 카운트)
                    elif candidate[idx] in query_digits:
                        ball += 1
            
                # 하나라도 카운트 결과가 다르면 이 후보는 탈락!
                if strike != target_c1 or ball != target_c2:
                    is_valid = False
                    break

            # 모든 질문을 완벽히 만족했다면 가능한 정답 후보
            if is_valid:
                answer += 1

print(answer)