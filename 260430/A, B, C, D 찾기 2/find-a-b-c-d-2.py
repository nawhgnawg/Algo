nums = list(map(int, input().split()))

nums.sort()

n = len(nums)
# [3, 3, 4, 6, 7, 7, 7, 10, 10, 10, 11, 13, 14, 14, 17]

a = nums[0]                
b = nums[1]
total = nums[14]    # 가장 큰 값 - 마지막 값

# C를 결정하기 위한 완전 탐색
for i in range(2, n):
    c = nums[i]
    d = total - a - b - c

    # 조건: B <= C <= D 인지 확인
    if b <= c <= d:
        possible_sums = [a, b, c, d, a + b, b + c, c + d, d + a, a + c,
                         b + d, a + b + c, a + b + d, a + c + d, 
                         b + c + d, a + b + c + d]

    if sorted(possible_sums) == nums:
        print(a, b, c, d)
        break
