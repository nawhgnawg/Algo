n = int(input())
a = [int(input()) for _ in range(n)]

answer = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            is_carry = False
            
            x, y, z = a[i], a[j], a[k]
            while x > 0 or y > 0 or z > 0:
                digit_sum = (x % 10) + (y % 10) + (z % 10)

                if digit_sum >= 10:
                    is_carry = True
                    break
                
                x //= 10
                y //= 10
                z //= 10
            
            if not is_carry:
                answer = max(answer, a[i] + a[j] + a[k])
            
            
print(answer)