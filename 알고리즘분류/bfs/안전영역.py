from collections import deque

N = int(input())
queue = deque()

board = [list(map(int, input().split())) for _ in range(N)]

arr = [[0] * N for _ in range(N)]

num_set = set()

for i in range(N):
    for j in range(N):
        num_set.add(board[i][j])

num_list = list(num_set)
num_list.sort()

result_list = [0] * 100

visited = [[False] * N for _ in range(N)]

dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]


def bfs(row, col):
    visited[row][col] = True
    queue.append((row, col))

    while queue:
        pop_row, pop_col = queue.popleft()

        for i in range(4):
            new_row = pop_row + dRow[i]
            new_col = pop_col + dCol[i]
            if (
                0 <= new_row < N
                and 0 <= new_col < N
                and visited[new_row][new_col] == False
                and arr[new_row][new_col] == 0
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))


for num in num_list:
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= num:
                arr[i][j] = 1
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j] == False:
                bfs(i, j)
                result_list[num] += 1

answer = max(result_list)
if answer == 0:
    print(1)
else:
    print(answer)
