from sys import stdin
import heapq

input = stdin.readline

# V: 정점의 개수 E: 간선의 개수
V, E = map(int, input().split())

# K: 시작 정점의 번호
K = int(input())

# 그래프 초기화
array = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v (가중치 w)
    array[u].append((v, w)) # (도착노드, 가중치)

INF = 1e8
distance = [INF] * (V + 1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 거리 0, 시작 노드
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue) # 거리, 노드   

        for neighbor, weight in array[now]:
            cost = dist + weight

            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(queue, (cost, neighbor))

# 다익스트라 실행
dijkstra(K)

# 결과 출력
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

    
