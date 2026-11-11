word = input()

max_len = 0
left = 0
seen = set()  # 현재 윈도우에 포함된 문자들을 저장할 집합

for right in range(len(word)):
    # 새로 들어온 문자가 이미 seen에 있다면, 중복이 사라질 때까지 left를 우측으로 이동
    while word[right] in seen:
        seen.remove(word[left])
        left += 1
    
    seen.add(word[right])

    current_len = right - left + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)