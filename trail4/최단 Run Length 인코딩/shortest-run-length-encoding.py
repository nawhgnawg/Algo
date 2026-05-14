A = input()

min_length = float('inf')

# Shift 하는 횟수: len(A)
for shift in range(len(A)):
    if shift == 0:
        shift_A = A
    else:
        shift_A = A[-shift:] + A[:-shift]    
    
    encoing_string = ''

    # 첫번째 문자로 초기화
    current_char = shift_A[0]
    count = 1

    # 두번째 문자부터 읽으며 비교
    for i in range(1, len(A)):
        if shift_A[i] == current_char:
            count += 1
        else:
            # 다른 문자가 등장하면 지금까지 쌓은 문자 + 개수 정산
            encoing_string += current_char + str(count)
            # 새로운 문자로 타겟 변경 및 카운트 초기화
            current_char = shift_A[i]
            count = 1 
            
    # 루프가 끝난 후, 미처 정산되지 못한 맨 마지막 문자열 그룹 추가
    encoing_string += current_char + str(count)

    # 최솟값 갱신
    min_length = min(len(encoing_string), min_length)

    # print(f'shift {shift}: {shift_A} -> {encoing_string}')

print(min_length)
    
