# 0: 빈칸 1: 벽 2: 바이러스
# 2가 있는 칸에서 바이러스가 퍼진다고할때 마지막에 0의 개수 출력
# N: 세로 M: 가로

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

from collections import deque

from itertools import combinations

import copy

zero_arr = []

queue = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
temp_board = []


def bfs(row, col):
    global temp_board
    visited[row][col] = True
    tup = (row, col)
    queue.append(tup)

    while queue:
        pop = queue.popleft()

        pop_row = pop[0]
        pop_col = pop[1]

        for i in range(4):
            temp_row = pop_row + dy[i]
            temp_col = pop_col + dx[i]

            if 0 <= temp_row < N and 0 <= temp_col < M:
                if temp_board[temp_row][temp_col] != 1:
                    if not visited[temp_row][temp_col]:
                        visited[temp_row][temp_col] = True
                        temp_board[temp_row][temp_col] = 2
                        queue.append((temp_row, temp_col))


for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            zero_arr.append((row, col))

combi = list(combinations(zero_arr, 3))

count_arr = []

for com in combi:
    temp_board = copy.deepcopy(board)
    visited = [[False] * M for _ in range(N)]

    temp_board[com[0][0]][com[0][1]] = 1
    temp_board[com[1][0]][com[1][1]] = 1
    temp_board[com[2][0]][com[2][1]] = 1

    for row in range(N):
        for col in range(M):
            if not visited[row][col] and temp_board[row][col] == 2:
                bfs(row, col)

    count = 0
    for row in range(N):
        for col in range(M):
            if temp_board[row][col] == 0:
                count += 1
    count_arr.append(count)
print(max(count_arr))
