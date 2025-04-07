import sys

input = sys.stdin.readline

N, M = map(int, input().split())

max_number_each_row = []

for _ in range(N):
    array = list(map(int, input().split()))
    array.sort()
    max_number_each_row.append(array[0])

print(max(max_number_each_row))


