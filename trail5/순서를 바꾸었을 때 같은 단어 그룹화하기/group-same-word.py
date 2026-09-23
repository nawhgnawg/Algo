from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

sorted_words = []

# 각 단어를 정렬하여 정규화하기
for word in words:
    # (1) sorted(word): 문자열을 알파벳 순으로 정렬하여 '리스트'로 반환합니다.
    # 예: 'cat' -> ['a', 'c', 't']
    char_list = sorted(word)

    # (2) ''.join(...): 글자 리스트를 다시 하나의 '문자열'로 합칩니다.
    # 예: ['a', 'c', 't'] -> 'act'
    sorted_string = ''.join(char_list)

    # (3) 결과 리스트에 담습니다.
    sorted_words.append(sorted_string)

# 정렬된 단어들의 빈도수 카운팅
counts = Counter(sorted_words)

# 가장 큰 그룹의 단어 개수 출력
print(max(counts.values()))