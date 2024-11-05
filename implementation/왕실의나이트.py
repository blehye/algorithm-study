# 8X8 좌표 평면에 나이트 위치가 주어졌을때 이동할 수 있는 경우의 수 출력
# 행 : 1 ~ 8
# 열 : a ~ h

import sys

input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

count = 0


def check_valid(x, y):
    if x < 1 or x > 8 or y < 1 or y > 8:
        return False
    return True


def get_night_coordinate(input):
    col = input[:1]
    row = input[1:]

    col = ord(col) - 96
    row = int(row)
    return col, row


user_input = input().rstrip()

x, y = get_night_coordinate(user_input)

for i in range(8):
    changed_x = x + dx[i]
    changed_y = y + dy[i]
    if check_valid(changed_x, changed_y):
        count += 1
print(count)
