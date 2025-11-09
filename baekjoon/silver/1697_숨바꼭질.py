# N: 수빈 위치, K: 동생 위치
# 수빈 이동 경우의 수 : x+1, x-1, 2*x

from collections import deque

visited = [False] * 100001

N, K = map(int, input().split())

def bfs(N, K, visited):
    queue = deque()
    queue.append((N, 0)) # 수빈 위치, 이동한 횟수
    visited[N] = True

    while queue:
        n, move_count = queue.popleft()

        if n == K:
            return move_count

        # 수빈 이동 경우의 수
        case_list = [n+1, n-1, 2*n]
        
        for case in case_list:
            if 0<=case<=100000 and not visited[case]:
                queue.append((case, move_count+1))
                visited[case] = True


print(bfs(N, K, visited))