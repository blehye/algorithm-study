from collections import deque

N = int(input())

dx = [0, 0, -1, 1] # 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
array = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []

def bfs(i, j):
    # 큐, 집의 수 초기화
    queue = deque()
    house_count = 0

    queue.append((i,j)) # 행, 렬
    house_count += 1
    visited[i][j] = True

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0<= ny < N and 0<= nx < N and array[ny][nx] == 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
                house_count += 1
    return house_count


for i in range(N):
    for j in range(N):
        # 아직 방문하지 않았으면서 1일때 bfs 돌리기
        if not visited[i][j] and array[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for count in result:
    print(count)