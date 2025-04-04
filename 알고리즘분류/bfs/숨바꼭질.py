from collections import deque

queue = deque()

# N: 수빈이의 위치, K: 동생의 위치
N, K = map(int, input().split())

visited = set()


def bfs(N, K, depth):
    if N == K:
        return depth
    queue.append((N, depth))
    visited.add(N)

    while queue:
        pop = queue.popleft()
        num = pop[0]
        dep = pop[1]

        case1 = num - 1
        case2 = num + 1
        case3 = num * 2

        if case1 == K or case2 == K or case3 == K:
            return dep + 1

        if 0 <= case1 <= 100000 and case1 != K and case1 not in visited:
            visited.add(case1)
            queue.append((case1, dep + 1))
        if 0 <= case2 <= 100000 and case2 != K and case2 not in visited:
            visited.add(case2)
            queue.append((case2, dep + 1))
        if 0 <= case3 <= 100000 and case3 != K and case3 not in visited:
            visited.add(case3)
            queue.append((case3, dep + 1))


print(bfs(N, K, 0))
