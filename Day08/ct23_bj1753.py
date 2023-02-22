# 백준 1753 => 최단경로
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())    # 노드의 개수, 엣지의 수
K = int(input())  # 시작노드
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V + 1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())   # u  --> v 노드의 방향, w는 가중치
    myList[u].append((v, w))

q.put((0, K))   # 시작점 K   queue 넣을때는 가중치, 노드순
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))   # 가중치로 오름차준

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")

