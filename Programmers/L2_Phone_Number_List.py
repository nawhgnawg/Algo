# 프로그래머스 Level 2 - 전화 번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 이전 풀이
# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
#             return False
#     return True


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]              # return false
# phone_book = ["123", "456", "789"]                          # return true
# phone_book = ["12", "123", "1235", "567", "88"]             # return false
print(solution(phone_book))