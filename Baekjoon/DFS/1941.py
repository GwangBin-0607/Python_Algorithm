graph = ['YYYYY', 'SYSYS', 'YYYYY', 'YSYYS', 'YYYYY']
stack = []
def dfs(y, x):
    global stack
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False
    if len(stack) < 7:
        stack.append(graph[y][x])
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
    
    if stack.count('S') >= 4:
        return True
    else:
        return False
dfs(0, 0)

        

        
