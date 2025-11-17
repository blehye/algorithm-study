from collections import deque
from itertools import combinations
import copy

# N: 세로, M: 가록
N, M = map(int, input().split()) 

# 벽 개수
WALL_COUNT = 3

# 상,하,좌,우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 연구소
array_origin = [list(map(int, input().split())) for _ in range(N)]
visited_origin = [[False] * M for _ in range(N)]

# max area
max_area = 0

def bfs(array, visited, all_2_coord):
    global max_area
    queue = deque()

    # 모든 2를 큐에 넣음
    for coord in all_2_coord:
        queue.append(coord)

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=ny<N and 0<=nx<M and array[ny][nx] == 0 and not visited[ny][nx]:
                array[ny][nx] = 1
                queue.append((ny, nx))
                visited[ny][nx] = True
    
    count_0 = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                count_0 += 1
    if max_area < count_0:
        max_area = count_0


# 연구소의 0을 3개 뽑는 경우의 수
coord_0_array = [(i, j) for i in range(N) for j in range(M) if array_origin[i][j] == 0]
coord_2_array = [(i, j) for i in range(N) for j in range(M) if array_origin[i][j] == 2]

for coord_0_com in combinations(coord_0_array, WALL_COUNT):
    array = copy.deepcopy(array_origin)
    visited = copy.deepcopy(visited_origin)
    for (i, j) in coord_0_com:
        array[i][j] = 1
    bfs(array, visited, coord_2_array)


print(max_area)
