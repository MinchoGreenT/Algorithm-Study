N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
result = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

while i <= 

print(result)
