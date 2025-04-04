import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
M = int(input())

array.sort()

start = 0
end = array[-1]
result = 0

while start <= end:
    middle = (start + end) // 2
    total = 0
    for item in array:
        total += min(item, middle)

    if total <= M:
        result = middle  
        start = middle + 1
    else:
        end = middle - 1

print(result)