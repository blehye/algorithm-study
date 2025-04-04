# N 입력값을 받으면 N!을 출력
# 팩토리얼 점화식 : N! = N * (N-1)!


N = int(input())


def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N - 1)


print(factorial(N))
