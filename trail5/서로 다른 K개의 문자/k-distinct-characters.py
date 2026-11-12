from collections import defaultdict

word, k = input().split()
k = int(k)

count_map = defaultdict(int)
max_len = 0
left = 0

for right in range(len(word)):
    # 1. right 문자를 윈도우에 추가
    count_map[word[right]] += 1

    # 2. 서로 다른 문자의 종류가 K개를 초과하면, left를 당기며 줄임
    while len(count_map) > k:
        count_map[word[left]] -= 1
        # 개수가 0이 되면 딕셔너리에서 키를 삭제하여 종류 수 관리
        if count_map[word[left]] == 0:
            del count_map[word[left]]
        
        left += 1
    
    # 3. 최장 길이 갱신
    current_len = right - left + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)
