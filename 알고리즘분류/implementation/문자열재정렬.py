import sys

input = sys.stdin.readline

# 알파벳 대문자와 숫자로만 구성된 문자열이 입력됨
# 모든 알파벳을 오름차순으로 정렬하여 출력, 모든 숫자 더한값 출력

arr = list(input().rstrip())

num_arr = []

for item in arr:
    if item.isdigit():
        num_arr.append(int(item))

for item in num_arr:
    arr.remove(str(item))

arr.sort()

print("".join(arr) + str(sum(num_arr)))
