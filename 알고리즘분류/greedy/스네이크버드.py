import sys

input = sys.stdin.readline

N, L = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

for i in array:
    if i <= L:
        L += 1
    else:
        break

print(L)