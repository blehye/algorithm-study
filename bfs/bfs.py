# 시작 노드를 큐에 넣음
# 큐에서 하나 꺼내서 방문하지 않은 인접한 노드를 큐에 넣음
# 큐에 원소가 다 없어질때까지 수행

from collections import deque

queue = deque()
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9


def bfs(node):
    queue.append(node)
    visited[node] = True
    print(node)

    while queue:
        pop = queue.popleft()

        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i)


bfs(1)
