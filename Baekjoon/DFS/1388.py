
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(input())
visited = [[False] * m for _ in range(n)]

def dfs(y, x, pre):
    if y < 0 or y >= n or x < 0 or x >= m:
        return False
    if visited[y][x] == False:
        if pre != '' and pre != graph[y][x]:
            return True
        visited[y][x] = True
        if graph[y][x] == '-':
            dfs(y, x + 1, graph[y][x])
            return True
        if graph[y][x] == '|':
            dfs(y + 1, x, graph[y][x])
            return True
        return False
    return False
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, '') == True:
            result += 1
print(result)
