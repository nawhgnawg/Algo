# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)




# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print(fac(5))

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
