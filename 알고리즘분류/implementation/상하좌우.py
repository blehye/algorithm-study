import sys

# 첫째줄에 공간의 크기 N 주어짐
# 가장 왼쪽 위 좌표는 (1,1) 가장 오른쪽 아래 좌표는 (N,N)
# 시작 좌표는 (1,1)
# 둘째줄에 이동할 계획서 내용이 주어짐
# 최종적으로 도착할 지점의 좌표 출력

input = sys.stdin.readline

# 공간의 크기
N = int(input().rstrip())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid(x, y):
    if x < 1 or y < 1 or x > N or y > N:
        return False
    return True


def move(plan, x, y):
    origin_x = x
    origin_y = y

    if plan == "U":
        x += dx[0]
        y += dy[0]
    elif plan == "D":
        x += dx[1]
        y += dy[1]
    elif plan == "L":
        x += dx[2]
        y += dy[2]
    elif plan == "R":
        x += dx[3]
        y += dy[3]

    if is_valid(x, y):
        return x, y
    return origin_x, origin_y


def solution():
    # 계획서
    plan_list = input().rstrip().split(" ")

    result_x = 1
    result_y = 1
    for plan in plan_list:
        result_x, result_y = move(plan, result_x, result_y)
    print(str(result_x) + " " + str(result_y))


solution()
