n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# 두 줄을 하나의 벨트로 합치기
belt = u + d

# t초 동안 회전시키기
shift = t % (2 * n)

# 슬라이딩을 이용해 한번에 회전
# 뒤쪽의 shift만큼을 앞으로 가져오고, 나머지를 뒤에 붙임
belt = belt[-shift:] + belt[:-shift]

print(*(belt[:n]))
print(*(belt[n:]))

    
            
