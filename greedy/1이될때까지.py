import sys

# N이 1이 될때까지 두 과정 중 하나를 반복적으로 선택 수행
# 1. N - 1
# 2. N / K (단 K로 나누어 떨어질때만 수행 가능)


def substract(N):
    return N - 1


def devide(N, K):
    return N // K


def processing(N, K):
    if N % K == 0:
        return devide(N, K)
    return substract(N)


def isNotOne(N):
    return N != 1


def solution(N, K):
    count = 0
    while isNotOne(N):
        N = processing(N, K)
        count += 1
    return count


input = sys.stdin.readline().rstrip()

N, K = map(int, input.split())

print(solution(N, K))
