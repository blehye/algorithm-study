from collections import deque

queue = deque()

M, N = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

is_zero = False # 안익은 토마토가 있는지 체크용

# 시작
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            is_zero = True
        if array[i][j] == 1:
            queue.append((i, j, 0))

# 익은 토마토 밖에 없다면 0 출력
if not is_zero:
    print(0)
    exit()

def bfs(queue, M, N, array):
    date_count = 0

    while queue:
        y, x, date = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<M and 0<=ny<N  and array[ny][nx]==0:
                queue.append((ny, nx, date+1))
                array[ny][nx] = 1
                date_count = date+1
    return date_count

# 토마토 익히기
date_count = bfs(queue, M, N, array)

# 토마토가 모두 익지 못하는 상황이면 -1 출력
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            print(-1)
            exit()

print(date_count)