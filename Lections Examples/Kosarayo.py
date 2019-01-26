"""MIPT Python Course Lection 25"""
visited = [False]
ans = []


def dfs(start, G, visited):
    visited[start] = True
    for u in G[start]:
        if not visited[u]:
            dfs()

    ans.append(start)
    for i in range(1, u+1):
        if not visited[i]:
            dfs(i, G, visited, ans)
     ans[i] = ans[::-1]





