import sys

input = sys.stdin.readline


def longest_palindrome_len(s: str) -> int:
  if not s:
    return 0

  # 1. 구분자 '#'을 삽입해 홀수/짝수 길이를 통일
  t = '#' + '#'.join(s) + '#'
  n = len(t)
  p = [0] * n  # p[i]: i를 중심으로 하는 회문 반지름

  center = 0  # 현재까지 가장 오른쪽까지 뻗은 회문의 중심
  right = 0  # 현재 회문이 닿은 가장 오른쪽 경계

  for i in range(n):
    # right보다 안쪽에 있으면 대칭 위치(mirror)의 반지름을 초기값으로 활용
    if i < right:
      mirror = 2 * center - i
      p[i] = min(right - i, p[mirror])

    # 양쪽으로 확장 가능한 만큼 늘리기
    while (
        i - p[i] - 1 >= 0
        and i + p[i] + 1 < n
        and t[i - p[i] - 1] == t[i + p[i] + 1]
    ):
      p[i] += 1

    # i에서 뻗어나간 범위가 기존 right를 넘어서면 중심과 경계 갱신
    if i + p[i] > right:
      center = i
      right = i + p[i]

  # 변환된 문자열 '#a#b#a#'에서 최대 반지름 값 == 원래 문자열의 최장 길이
  return max(p)


s = input().strip()
print(longest_palindrome_len(s))