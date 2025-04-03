import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

x = int(input())

array.sort()

start = 0
end = len(array) - 1
count = 0

while start != end:
    sum = array[start] + array[end]
    if sum == x:
        count += 1
    if sum <= x:
        start += 1
    else:
        end -= 1
        

print(count)