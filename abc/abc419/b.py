Q = int(input())

import heapq

heap = []

for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    heapq.heappush(heap, query[1])
  elif query[0] == 2:
    print(heapq.heappop(heap))