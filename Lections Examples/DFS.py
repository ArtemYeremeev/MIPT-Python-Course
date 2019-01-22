"""MIPT Python Course Lection 23"""

def dfs(Vertex, G, used):
    used.add(Vertex)
    for neibour in G[Vertex]:
        if neibour not in used:
            dfs(neibour, G, used=0)
used = {}
N = 0
for Vertex in G:
    if Vertex not in used:
        dfs()
        N += 1
print(N)



