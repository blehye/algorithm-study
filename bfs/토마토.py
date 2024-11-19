from collections import deque

queue = deque()

# M: 가로 N: 세로 H: 높이
M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]

zero_count = 0

# 상, 하, 좌, 우, 앞, 뒤
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 0, 0, -1, 1]
dm = [0, 0, 1, -1, 0, 0]


def bfs():
    global zero_count
    while queue:
        pop_h, pop_n, pop_m, pop_depth = queue.popleft()

        # 6가지 경우의 수
        for i in range(6):
            h = pop_h + dh[i]
            n = pop_n + dn[i]
            m = pop_m + dm[i]
            if (
                0 <= h < H
                and 0 <= n < N
                and 0 <= m < M
                and visited[h][n][m] == False
                and box[h][n][m] == 0
            ):
                visited[h][n][m] = True
                box[h][n][m] = 1
                zero_count -= 1
                if zero_count == 0:
                    return pop_depth + 1
                queue.append((h, n, m, pop_depth + 1))
    return -1


for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((h, n, m, 0))
            elif box[h][n][m] == 0:
                zero_count += 1

if zero_count == 0:
    print(0)
    exit()

print(bfs())
