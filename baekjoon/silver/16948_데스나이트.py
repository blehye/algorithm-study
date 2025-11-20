from collections import deque
from sys import stdin

input = stdin.readline

N = int(input()) # 체스판 크기

r1, c1, r2, c2 = map(int, input().split()) # 시작 위치, 종료 위치

dx = [-1, +1, -2, +2, -1, +1]
dy = [-2, -2, 0, 0, +2, +2]


# 데스나이트가 시작 위치에서 종료 위치로 이동하는 최소 이동 횟수

visited = [[False] * N for _ in range(N)]

def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        y, x, count = queue.popleft()
        if y==r2 and x==c2:
            return count
        
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                queue.append((ny, nx, count+1))
                visited[ny][nx] = True
    return -1

print(bfs(r1, c1))



