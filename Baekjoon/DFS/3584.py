import sys
sys.setrecursionlimit(100000)
def dfs(x,result):
    result.append(x)
    if tree[x]:
        for i in tree[x]:
            dfs(i, result)


t = int(input())
for i in range(t):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for j in range(n - 1):
        p, c = map(int, input().split())
        tree[c].append(p)
    a_result = []
    b_result = []
    a, b = map(int, input().split())
    dfs(a, a_result)
    dfs(b, b_result)
    sol = 0
    for i in a_result:
        for j in b_result:
            if i == j:
               sol = i
               break
        else:
            continue
        break
    print(sol)

