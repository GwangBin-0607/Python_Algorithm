from collections import deque
computer = int(input())
graph = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)
for _ in range(int(input())):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p) //이거!
if graph[1]:
    queue = deque()
    visited[1] = True
    queue.append(1)
    while queue:
        left = queue.popleft()
        for i in graph[left]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
print(visited)
print(visited.count(True) - 1)
        
            
                   
            
