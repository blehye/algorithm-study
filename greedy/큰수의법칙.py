import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

first = array[-1]
second = array[-2]

# 가장 큰 수가 K번 연속으로 더해질 수 있는 횟수

count = (M // (K + 1)) * K
count += M % (K + 1)
result = 0
result += (count) * first
result += (M - count) * second
print(result)

