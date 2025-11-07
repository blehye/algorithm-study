from collections import deque

queue = deque()
N, M = map(int, input().split())
array = [[int(i) for i in input()] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, -1, 1] # 상, 하, 좌, 우
dy = [1, -1, 0, 0]

def bfs():
    queue.append((0,0,1))
    visited[0][0] = True

    while queue:
        y, x, distance = queue.popleft()
        if y == N-1 and x == M-1:
            print(distance)
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < N and 0<= nx < M and array[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx, distance + 1))
                visited[ny][nx] = True

bfs()
