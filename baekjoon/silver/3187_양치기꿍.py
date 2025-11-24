from collections import deque
from sys import stdin

input = stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())

array = [list(map(str, input().rstrip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

result_k_count = 0
result_v_count = 0

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    global result_k_count
    global result_v_count

    k_count = 0
    v_count = 0

    target = array[i][j]
    if target == "k":
        k_count += 1
    elif target == "v":
        v_count += 1



    while queue:
        y, x = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<M and 0<=ny<N and array[ny][nx] != "#" and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
                if array[ny][nx] == "k":
                    k_count += 1
                elif array[ny][nx] == "v":
                    v_count += 1
    if k_count > v_count:
        result_k_count += k_count
    else:
        result_v_count += v_count


for i in range(N):
    for j in range(M):
        if array[i][j] != "#" and not visited[i][j]:
            bfs(i, j)

print(result_k_count, result_v_count)

