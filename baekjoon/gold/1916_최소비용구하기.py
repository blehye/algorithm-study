from sys import stdin
import heapq

input = stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수

array = [[] for _ in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)

for _ in range(1, M+1):
    u, v, w = map(int, input().split())
    array[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for neighbor, weight in array[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(queue, (cost, neighbor))

dijkstra(start)
print(distance[end])


