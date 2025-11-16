from collections import deque
from sys import stdin

import copy

input = stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = [[-1] * m for _ in range(n)]

def bfs(i, j):
    global array
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        y, x, count = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<m and 0<=ny<n and array[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx, count+1))
                visited[ny][nx] = True
                result[ny][nx] = count+1

# 2좌표에서 bfs
for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            result[i][j] = 0
            bfs(i, j)
        if array[i][j] == 0:
            result[i][j] = 0

for i in range(n):
    print(*result[i])

