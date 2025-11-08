from collections import deque

computer_count = int(input())
set_count = int(input())
queue = deque()
visited = [False] * (computer_count + 1)

linked_info = [[] for _ in range(computer_count + 1)]

for _ in range(set_count):
    x, y = map(int, input().split())
    linked_info[x].append(y)
    linked_info[y].append(x)

def bfs():
    queue.append(1)
    visited[1] = True

    while queue:
        target_computer = queue.popleft()
        for item in linked_info[target_computer]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True

bfs()
print(visited.count(True)-1)

