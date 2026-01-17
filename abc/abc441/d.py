N, M, L, S, T = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    graph[U].append((V, C))

# dp[v] = 頂点1から現在のステップ数で頂点vに到達したときのコストの集合
dp = [set() for _ in range(N + 1)]
dp[1].add(0)

for _ in range(L):
    next_dp = [set() for _ in range(N + 1)]
    for u in range(1, N + 1):
        for c in dp[u]:
            for v, cost in graph[u]:
                new_cost = c + cost
                if new_cost <= T:
                    next_dp[v].add(new_cost)
    dp = next_dp

result = []
for v in range(1, N + 1):
    for c in dp[v]:
        if S <= c <= T:
            result.append(v)
            break

result.sort()
print(*result)