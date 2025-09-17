# 프로그래머스 Level 3 - 베스트 엘범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579


# def solution(genres, plays):
#     answer = []
#     dic = {}
#     dic_two = {i: [] for i in genres}
#     for i, genre in enumerate(genres):
#         dic[genre] = dic.get(genre, 0) + plays[i]
#         dic_two[genre].append(plays[i])
#         dic_two[genre].sort(reverse=True)
#     print(dic)
#     print(dic_two)
#     high = max(dic)
#     print(dic_two[high])
#     for i in range(len(dic_two[high])):
#         answer.append(plays.index(dic_two[i]))
#
#     return answer


def solution(genres, plays):
    answer = []
    genre_total = {}  # 장르별 총 재생 수
    genre_songs = {}  # 장르별 노래 (재생 수, 인덱스)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] = genre_total.get(g, 0) + p
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))   # 재생 수랑, index를 같이 저장

    # ✅장르별로 재생 수 내림차순, 같으면 인덱스 오름차순
    for g in genre_songs:
        genre_songs[g].sort(key=lambda x: (-x[0], x[1]))

    # 총 재생 수로 장르 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    # sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x])

    for g in sorted_genres:
        answer.extend([idx for _, idx in genre_songs[g][:2]])  # 상위 2곡 선택

    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]     # return [4, 1, 3, 0]
print(solution(genres, plays))