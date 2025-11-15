from collections import deque
from sys import stdin

input = stdin.readline

# F: 총 층수, S: 현재 층, G: 사무실 층, U: 위로가는충수, D: 아래로가는층수
F, S, G, U, D = map(int, input().split())

# S -> G층으로 가기 위해 눌러야 하는 버튼 수의 최솟값 출력해라


visited = [False] * (F + 1)

def bfs():
    queue = deque()
    queue.append((S, 0))
    visited[S] = True

    while queue:
        floor, count = queue.popleft()

        if floor == G:
            return count
        
        case1 = floor + U
        case2 = floor - D
        
        if 1<=case1<=F and not visited[case1]:
            queue.append((case1, count+1))
            visited[case1] = True

        if 1<=case2<=F and not visited[case2]:
            queue.append((case2, count+1))
            visited[case2] = True
    return "use the stairs"

print(bfs())
        