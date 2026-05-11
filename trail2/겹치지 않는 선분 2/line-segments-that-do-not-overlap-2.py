n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    # i번째 선분이 다른 어떤 선분과도 교차하지 않는지 여부를 저장할 변수
    is_crossed = False
    
    start_i, end_i = lines[i]

    for j in range(n):
        # 자신은 패스
        if i == j:
            continue
        
        start_j, end_j = lines[j]

        # 선분 i와 선분 j가 서로 교차하는 조건
        # 1. i의 시작점은 j보다 왼쪽인데, 끝점은 j보다 오른쪽인 경우 (i가 j를 교차)
        # 2. i의 시작점은 j보다 오른쪽인데, 끝점은 j보다 왼쪽인 경우 (j가 i를 교차)
        # 시작점의 대소 관계와 끝점의 대소 관계가 반대 방향인지 확인
        # (하나의 대소 차이는 양수인데, 다른 하나는 음수라면 곱했을 때 음수(< 0)가 됩니다)
        if (start_i - start_j) * (end_i - end_j) < 0:
            is_crossed = True
            break

    # 교차하지 않았다면 증가
    if not is_crossed:
        answer += 1

        # # 검사 시작점이 시작과 끝점 사이에 있고 검사 끝점이 끝점보다 작은 경우
        # if start < lines[j][0] <= end and lines[j][1] < end:
        #     break
        # # 검사 시작점은 시작점 이전에 있지만 검사 끝점이 끝점보다 큰 경우
        # if lines[j][0] < start and lines[j][1] > end:
        #     break
        
print(answer)