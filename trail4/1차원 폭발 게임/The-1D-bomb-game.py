n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    did_explode = False     # 이번턴에 폭발이 있었는지 기록
    next_bombs = []         # 살아남은 폭탄을 담을 새로운 배열

    length = len(numbers)
    if length == 0:
        break               # 폭탄이 다 타져서 없어지면 종료

    i = 0
    # 배열 전체를 훑으며 덩어리 찾기
    while i < length:
        j = i

        # 현재 폭탄과 연속해서 같은 숫자를 가진 폭탄의 끝지점 찾기
        while j < length and numbers[i] == numbers[j]:
            j += 1

        # 연속된 폭탄의 개수
        count = j - i

        # 1. M개 이상이면 터짐
        if count >= m:
            did_explode = True

        # 2. M개 미만이면 살아남음
        else:
            next_bombs.extend(numbers[i: j])

        # 다음 덩어리를 위해 인덱스 점프
        i = j

    # 살아남은 폭탄들을 원본 배열에 덮어쓰기
    numbers = next_bombs

    # 만약 배열을 다 돌았는데 폭발이 일어나지 않았다면 끝난것
    if not did_explode:
        break

print(len(numbers))
for b in numbers:
    print(b)

        
        
