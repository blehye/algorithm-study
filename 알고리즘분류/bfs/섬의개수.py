from collections import deque

queue = deque()

# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dRow = [-1, 1, 0, 0, -1, -1, 1, 1]
dCol = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(row, col):
    visited[row][col] = True
    queue.append((row, col))

    while queue:
        pop_row, pop_col = queue.popleft()

        for i in range(8):
            new_row = pop_row + dRow[i]
            new_col = pop_col + dCol[i]

            if (
                0 <= new_row < h
                and 0 <= new_col < w
                and visited[new_row][new_col] == False
                and board[new_row][new_col] == 1
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    land_count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                land_count += 1
    print(land_count)
