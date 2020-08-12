import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    link = tuple(map(int, input().split()))
    graph[link[0]].append(link[1])
    graph[link[1]].append(link[0])

visited = [False] * (N+1)
stack = []
def solve_dfs(v):
    stack.append(v)
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            solve_dfs(next_v)
    return
solve_dfs(1)
print(len(stack)-1)