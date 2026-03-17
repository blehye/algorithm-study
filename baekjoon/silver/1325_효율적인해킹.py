from collections import deque
from sys import stdin

input = stdin.readline

# N: 컴퓨터의 개수, M: 신뢰관계 개수
n, m = map(int, input().split())

array = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    # b를 해킹하면 a도 해킹할 수 있음
    a, b = map(int, input().split())
    array[b].append(a)

def bfs(start):
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(start)
    visited[start] = True
    count = 0

    while queue:
        node = queue.popleft()

        for item in array[node]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True
                count += 1
    return count

result = []       
max_count = 0

for computer_num in range(1, n + 1):
    count =  bfs(computer_num)
    max_count = max(max_count, count)
    result.append((computer_num, count))

for computer_num, count in result:
    if count == max_count:
        print(computer_num, end=" ")



