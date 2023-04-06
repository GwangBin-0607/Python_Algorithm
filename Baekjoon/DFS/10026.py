import sys
sys.setrecursionlimit(100000)
def dfs(y, x, pre):
    if y < 0 or y >= n or x < 0 or x >= n:
        return False
    if visited[y][x] == False:
        if pre != '' and pre != graph[y][x]:
            return True
        visited[y][x] = True
        cur = graph[y][x]
        dfs(y, x + 1, cur)
        dfs(y, x - 1, cur)
        dfs(y + 1, x, cur)
        dfs(y - 1, x, cur)
        return True
    return False

n = int(input())
visited = [[False] * n for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(input())

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, '') == True:
            result += 1
for i in range(n):
    new = graph[i].replace('G', 'R')
    graph[i] = new
visited = [[False] * n for _ in range(n)]

r_result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, '') == True:
            r_result += 1
print(result, r_result)
