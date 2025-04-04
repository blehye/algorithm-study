# N x M 미로
# 동빈이의 위치는 (1,1)
# 미로의 출구 (N, M)
# 한번에 한칸씩 이동
# 0: 괴물이 있는 부분, 1: 괴물이 없는 부분
# 미로는 반드시 탈출할수있음
# 탈출하기 위해 움직여야하는 최소 칸의 개수?

from collections import deque

queue = deque()

N, M = map(int, input().split())

board = [[int(char) for char in input()] for _ in range(N)]

visited = [[False] * M for _ in range(N)]

drow = [1, -1, 0, 0]
dcol = [0, 0, -1, 1]


def bfs(row, col, depth):
    visited[row][col] = True
    queue.append(((row, col), depth))

    while queue:
        pop = queue.popleft()
        pop_row = pop[0][0]
        pop_col = pop[0][1]
        depth = pop[1]

        if pop_row == N - 1 and pop_col == M - 1:
            return depth

        for i in range(4):
            new_pop_row = pop_row + drow[i]
            new_pop_col = pop_col + dcol[i]

            if 0 <= new_pop_row < N and 0 <= new_pop_col < M:
                if not visited[new_pop_row][new_pop_col]:
                    if board[new_pop_row][new_pop_col] == 1:
                        visited[new_pop_row][new_pop_col] = True

                        queue.append(((new_pop_row, new_pop_col), depth + 1))


print(bfs(0, 0, 1))
