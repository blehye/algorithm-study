from collections import deque, defaultdict

node_count = int(input())
tree = defaultdict(list)

for _ in range(node_count - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

parent = [0] * (node_count + 1)


def bfs(start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in tree[current]:
            if parent[neighbor] == 0:
                parent[neighbor] = current
                queue.append(neighbor)


bfs(1)

for i in range(2, node_count + 1):
    print(parent[i])
