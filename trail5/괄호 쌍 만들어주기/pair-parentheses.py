A = input()
count = 0
open_pairs = 0  # 지금까지 발견한 '(( ' 의 개수

for i in range(len(A) - 1):
    if A[i] == '(' and A[i + 1] == '(':
        # 여는 괄호 쌍을 발견하면 개수를 누적해 둡니다.
        open_pairs += 1
        
    elif A[i] == ')' and A[i + 1] == ')':
        # 닫는 괄호 쌍을 발견하면, 
        # 내 앞에 있던 모든 '(( ' 들과 짝을 지을 수 있으므로 누적된 개수만큼 정답에 더합니다.
        count += open_pairs

print(count)