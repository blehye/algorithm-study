from collections import deque
from sys import stdin

input = stdin.readline

# N: 세로, M: 가로, K: 음쓰 개수
N, M, K= map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

array = [[0] * (M+1) for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

for _ in range(K):
    r, c = map(int, input().split())
    array[r][c] = 1

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    result_count = 1

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 1<=ny<N+1 and 1<=nx<M+1 and array[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                result_count += 1
                visited[ny][nx] = True
    return result_count

result = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if array[i][j] == 1 and not visited[i][j]:
            x = bfs(i, j)
            result = max(x, result)

print(result)