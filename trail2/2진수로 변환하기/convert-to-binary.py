n = int(input())

if n == 0:
    print(0)
else:
    result = []

    while n > 0:
        result.append(str(n % 2))
        n = n // 2

    print("".join(result[::-1]))
    
        