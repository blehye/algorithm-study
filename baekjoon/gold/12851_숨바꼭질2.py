from collections import deque
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

MAX = 200001

result_count = 0
result_case = 1

def bfs():
    global result_count
    global result_case
    queue = deque()
    queue.append((n, 0))

    while queue:
        position, count = queue.popleft()

        if position == k:
            if result_count == 0:
                result_count = count
            elif result_count < count:
                break
            elif result_count == count:
                result_case += 1
        
        case1 = position+1
        case2 = position-1
        case3 = 2 * position

        if 0<= case1 <MAX:
            queue.append((case1, count+1))
        if 0<= case2 <MAX:
            queue.append((case2, count+1))
        if 0<= case3 <MAX :
            queue.append((case3, count+1))

bfs()
print(result_count)
print(result_case)