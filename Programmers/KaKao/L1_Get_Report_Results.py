# 프로그래머스 Level 1 - 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    report_mail_dict = {name: set() for name in id_list}
    report_count_dict = {name: 0 for name in id_list}
    # a -> b 신고
    for l in report:
        a, b = l.split()
        report_mail_dict[a].add(b)   # 누가 누굴 신고했는지

    # 각 유저가 신고한 사람들 기준으로 카운트 증가
    for reporter in report_mail_dict:
        for reported in report_mail_dict[reporter]:
            report_count_dict[reported] += 1

    # 기준 넘어가는지 확인
    report_list = []
    for name in id_list:
        if report_count_dict[name] >= k:
            report_list.append(name)

    # 메일 몇개 받는지 확인
    for name in id_list:
        count = 0
        for check in report_list:
            if check in report_mail_dict[name]:
                count += 1
        answer.append(count)

    return answer

# id_list, report, k = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2  # return [2, 1, 1, 0]
id_list, report, k = ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3  # return [0, 0]
print(solution(id_list, report, k))