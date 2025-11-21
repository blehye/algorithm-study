from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

array = [ list(map(int, input().rstrip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        y, x = queue.popleft()
        if y == N-1:
            return True
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<M and 0<=ny<N and array[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return False

for j in range(M):
    if array[0][j] == 0 and not visited[0][j]:
        if bfs(0, j):
            print("YES")
            exit()
print("NO")
