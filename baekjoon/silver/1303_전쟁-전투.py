from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

array = [[i for i in input()] for _ in range(M)]

visited = [[False] * N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

power1 = 0
power2 = 0

def bfs(key, i, j):
    result = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    result = 1

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<N and 0<=ny<M and array[ny][nx] == key and not visited[ny][nx]:
                result += 1
                queue.append((ny, nx))
                visited[ny][nx] = True
    return result * result

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            key = array[i][j]
            result = bfs(key, i, j)
            if key == "W":
                power1 += result
            else:
                power2 += result
print(power1, power2)