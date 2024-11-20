from collections import deque

test_count = int(input())

queue = deque()
board = []
visited = []

# 나이트의 이동 경우의 수
dRow = [-1, -2, -2, -1, 1, 2, 2, 1]
dCol = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(row, col):
    global board
    global visited
    global queue

    visited[row][col] = True
    queue.append((row, col, 0))

    while queue:
        pop_row, pop_col, pop_depth = queue.popleft()

        if board[pop_row][pop_col] == 1:
            return pop_depth

        for i in range(8):
            new_row = pop_row + dRow[i]
            new_col = pop_col + dCol[i]

            if (
                0 <= new_row < N
                and 0 <= new_col < N
                and visited[new_row][new_col] == False
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, pop_depth + 1))


for _ in range(test_count):
    N = int(input())  # 한변의 길이
    board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    if x == target_x and y == target_y:
        print(0)
        continue
    board[target_y][target_x] = 1
    queue = deque()
    print(bfs(y, x))
