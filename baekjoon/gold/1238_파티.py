from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

array = [[] for _ in range(N + 1)]
result_distance = [[]]


for _ in range(M):
    u, v, w = map(int, input().split())
    array[u].append((v, w))

def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for neighber, weight in array[now]:
            cost = dist + weight
            if cost < distance[neighber]:
                distance[neighber] = cost
                heapq.heappush(queue, (cost, neighber))

    return distance


for index in range(1, N + 1):
    result_distance.append(dijkstra(index)) 

anwser = 0

for index in range(1, N + 1):
    duration = result_distance[index][X] + result_distance[X][index]
    if anwser < duration:
        anwser = duration

print(anwser)