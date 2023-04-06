import sys
sys.setrecursionlimit(100000)
def dfs(r, c):
    if r < 0 or r >= h or c < 0 or c >= w:
        return False
    if m[r][c] == 1:
        m[r][c] = 0
        dfs(r - 1, c - 1)
        dfs(r - 1, c)
        dfs(r - 1, c + 1)
        dfs(r, c - 1)
        dfs(r, c + 1)
        dfs(r + 1, c - 1)
        dfs(r + 1, c + 1)
        dfs(r + 1, c)
        return True
    return False
while True:
    
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    m = []
    for _ in range(h):
        m.append(list(map(int, input().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1
    print(count)
