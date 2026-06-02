# 프로그래머스 Level 1 - 중요한 단어를 스포 방지
# https://school.programmers.co.kr/learn/courses/30/lessons/468370

def solution(message, spoiler_ranges):
    # 1. 단어들을 분리하며 각각의 시작/끝 인덱스를 저장
    words = []
    current_idx = 0
    for w in message.split(' '):
        word_start = current_idx
        word_end = current_idx + len(w) - 1
        words.append((w, word_start, word_end))

        # 다음 단어의 시작점 (+1은 공백 문자의 길이)
        current_idx += len(w) + 1

    spoiler_words = set()
    non_spoiler_words = set()

    # 2. 각 단어가 스포일러 구간에 걸치는지 판별
    for w, start, end in words:
        is_spoiler = False

        # 하나라도 겹치는 스포일러 구간이 있는지 확인
        for s, e in spoiler_ranges:
            if max(start, s) <= min(end, e):
                is_spoiler = True
                break

        # 스포일러 여부에 따라 알맞은 집합(Set)에 단어 추가
        if is_spoiler:
            spoiler_words.add(w)
        else:
            non_spoiler_words.add(w)

    # 3. 스포일러 단어 집합에서 일반 단어 집합에 존재하는 단어를 제외 (차집합)
    important_words = spoiler_words - non_spoiler_words

    # 4. 조건을 만족하는 고유한 중요 단어의 개수를 반환
    return len(important_words)