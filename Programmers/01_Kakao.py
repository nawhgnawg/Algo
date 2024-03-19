# 2023 KAKAO BLIND RECRUITMENT
# 프로그래머스 - 택배 배달과 수거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/150369

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

# 그리디
def solution1(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            print((n - 1) * 2)
            answer += (n - i) * 2

    return answer


# zip 이용
def solution2(cap, n, deliveries, pickups):
    # (거리, deliveries[i - 1], pickups[i - 1])
    idps = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups), 1) if d or p]
    delivery = 0
    pickup = 0
    answer = 0
    while idps:
        i, d, p = idps.pop()
        delivery += d
        pickup += p
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += i * 2
    return answer

#


print(solution2(cap, n, deliveries, pickups))