import sys

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

array.sort()

start = 0
end = len(array) - 1

result = []

while start != end:
    temp_start = array[start]
    temp_end = array[end]
    temp_sum = temp_start + temp_end
    if temp_sum == 0:
        print(temp_start, end=" ")
        print(temp_end, end="")
        break

