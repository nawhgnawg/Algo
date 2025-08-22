# PCCE 기출문제 10번 데이터 분석
# https://school.programmers.co.kr/learn/courses/19274/lessons/240605

data = [[1, 20300114, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
result = [[3, 20300401, 10, 8],[1, 20300104, 100, 80]]

def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = [d for d in data if d[dic[ext]] < val_ext]
    answer.sort(key=lambda x: x[dic[sort_by]])
    return answer

print(solution(data, ext, val_ext, sort_by))