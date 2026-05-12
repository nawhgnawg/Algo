n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# 직사각형 테두리를 시계 방향으로 1칸 회전하는 함수
def rotate_border(r1, c1, r2, c2):
    # 나중에 덮어써서 사라질 왼쪽 위 모서리 값을 미리 선언 
    temp = a[r1][c1]

    # 왼쪽 변: 아래에서 위로 올리기
    for i in range(r1, r2):
        a[i][c1] = a[i + 1][c1]
    
    # 아랫 변: 오른쪽에서 왼쪽으로 당기기
    for j in range(c1, c2):
        a[r2][j] = a[r2][j + 1]
    
    # 오른쪽 변: 위에서 아래로 내리기
    for i in range(r2, r1, -1):
        a[i][c2] = a[i - 1][c2]

    # 윗 변: 왼쪽에서 오른쪽으로 밀기
    for j in range(c2, c1, -1):
        a[r1][j] = a[r1][j - 1]

    # 미리 빼두었던 왼쪽 위 모서리 값을 바로 오른쪽 칸에 대입
    a[r1][c1 + 1] = temp

# 2. 직사각형 내부 모든 칸을 인접한 값들의 평균값으로 변환하는 함수
def set_averages(r1, c1, r2, c2):
    # 변화가 '동시에' 일어나야 하므로, 계산 결과를 임시 저장할 2D 배열 생성
    # row 대신 row[:]를 사용하는 이유는 row는 외관상으로는 새로운 리스트를 만드는 것처럼 보이지만,
    # 실제로는 내부에 있는 행(1차원 리스트)들의 '주소값(메모리 위치)'을 그대로 복사해오기 때문이다.
    # -> temp_grid를 바꾸면 원본 a도 바뀌어버림
    temp_grid = [row[:] for row in a]        

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 직사각형 영역 내부(테두리 포함) 전체 순회
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            total_sum = a[i][j]
            count = 1

            # 상하좌우 인접한 칸 확인
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    total_sum += a[nx][ny]
                    count += 1

            # 평균값(정수 버림)을 임시 배열에 기록
            temp_grid[i][j] = total_sum // count

    # 계산이 끝난 최종 평균값들을 한 번에 원본 배열 a에 반영
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            a[i][j] = temp_grid[i][j]


# 3. 메인 바람 시뮬레이션 루프 진행
for r1, c1, r2, c2 in winds:
    # 0-indexed 인덱스로 보정
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    # Step 1: 테두리 회전
    rotate_border(r1, c1, r2, c2)

    # Step 2: 회전된 배열을 기준으로 평균값 계산 및 반영
    set_averages(r1, c1, r2, c2)


# 4. 최종 결과 출력
for row in a:
    print(*(row))




# # 새로운 건물
# new_grid = [[0] * m for _ in range(n)]

# # 바람에 의해 시계 방향으로 회전
# for r1, c1, r2, c2 in winds:

#     # 좌표 인덱스 수정
#     r1 -= 1
#     c1 -= 1
#     r2 -= 1
#     c2 -= 1
    
#     # 테두리 배열
#     belt = a[r1][c1:]
#     for k in range(1, r2 - r1):
#         belt += [a[r1 + k][c2]]
#     belt += a[r2][:r1 - 1:-1]
#     for k in range(1, r2 - r1):
#         belt += [a[r2 - k][c1]]

#     # 바람 적용
#     belt = belt[-1:] + belt[:-1]


#     # 건물에 적용

#     for i in range(r1, r2 + 1):
#         for j in range(c1, c2 + 1):
#             # 윗변 아랫변
#             if i == r1 or i == r2:
                
#             # 양옆변
#             elif j == c1 or j == c2:
                
    
    

            


