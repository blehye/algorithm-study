# 수열이 오름차순으로 정렬되어있음
# 수열에서 x가 등장하는 횟수 계산

N, x = map(int, input().split())
array = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

print(bisect_right(array, x) - bisect_left(array, x))
