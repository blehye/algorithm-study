# 0: 뚫려있는 부분 1: 막혀있는 부분
# 얼려진 음료수가 총 몇개인지 구하라

from collections import deque

queue = deque()

N, M = map(int, input().split())

board = [[int(char) for char in input()] for _ in range(N)]

visited = [[False] * M for _ in range(N)]

drow = [1, -1, 0, 0]
dcol = [0, 0, -1, 1]


def bfs(row, col):
    visited[row][col] = True
    queue.append((row, col))

    while queue:
        pop = queue.popleft()
        pop_row = pop[0]
        pop_col = pop[1]

        for i in range(4):
            new_pop_row = pop_row + drow[i]
            new_pop_col = pop_col + dcol[i]

            if 0 <= new_pop_row < N and 0 <= new_pop_col < M:
                if not visited[new_pop_row][new_pop_col]:
                    if board[new_pop_row][new_pop_col] == 0:
                        visited[new_pop_row][new_pop_col] = True
                        queue.append((new_pop_row, new_pop_col))


count = 0
for row in range(N):
    for col in range(M):
        if board[row][col] == 0 and not visited[row][col]:
            bfs(row, col)
            count += 1

print(count)
