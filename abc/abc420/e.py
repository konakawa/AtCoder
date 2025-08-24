class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.active_count = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.active_count[root_x] += self.active_count[root_y]
        self.active_count[root_y] = 0
    
    def get_active_count(self, x):
        root = self.find(x)
        return self.active_count[root]
    
    def update_active(self, x, delta):
        root = self.find(x)
        self.active_count[root] += delta

N, Q = map(int, input().split())

states = [0] * N
uf = UnionFind(N)

results = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1] - 1, query[2] - 1
        uf.union(a, b)
    elif query[0] == 2:
        v = query[1] - 1
        states[v] ^= 1
        
        if states[v] == 1:
            uf.update_active(v, 1)
        else:
            uf.update_active(v, -1)
    elif query[0] == 3:
        v = query[1] - 1
        active_in_component = uf.get_active_count(v)
        
        if active_in_component > 0:
            results.append('Yes')
        else:
            results.append('No')

for result in results:
    print(result)