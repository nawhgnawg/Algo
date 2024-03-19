# 두 수의 합이 target을 만족하는 수 찾기

num = [16, 8, 23, 4, 15]
target = 19

def two_sum(num, target):
    hashMap = {}
    for idx, val in enumerate(num):
        another = target - val
        if another in hashMap:
            return [hashMap[another], idx]
        else:
            hashMap[val] = idx
            print(hashMap)
    return [-1, 1]

print(two_sum(num, target))