import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split())
area = []
for i in range(k):
    area.append(list(map(int, input().split())))

graph = [[0] * m for _ in range(n)]
for i in area:
    op = (i[0], i[1])
    np = (i[2], i[3])
    for x in range(op[0], np[0]):
        for y in range(op[1], np[1]):
           graph[y][x] = 1

count = 0
def dfs(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return False
    if graph[y][x] == 0:
        global count
        count += 1
        graph[y][x] = 1
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    
    return False
result = []
for i in range(n):
    for j in range(m):
        count = 0
        if dfs(i, j) == True:
            result.append(count)

result.sort()
print(len(result))
print(*result)

