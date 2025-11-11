from collections import deque

dx = [0 , 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())


def bfs(i, j, M, N, array, visited):
    # 큐 초기화 
    queue = deque()

    queue.append((i, j))
    visited[i][j] = True

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0<= ny < N and not visited[ny][nx] and array[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True

def process():
    # 지렁이 개수 초기화
    worm_count = 0
    # 가로, 세로, 배추개수 초기화
    M, N, bechu_count = map(int, input().split())
    # 행렬 초기화
    array = [[0] * M for _ in range(N)]
    # 방문정보 초기화
    visited = [[False] * M for _ in range(N)]

    for _ in range(bechu_count):
        x, y = map(int, input().split())
        array[y][x] = 1

    for i in range(N):
        for j in range(M):
            if array[i][j] == 1 and not visited[i][j]:
                bfs(i, j, M, N, array, visited)
                worm_count += 1
    # 지렁이 개수 리턴
    return worm_count


for _ in range(T):
    worm_count = process()
    print(worm_count)

