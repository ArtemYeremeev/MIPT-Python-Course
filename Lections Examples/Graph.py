"""MIPT Python Course Lections 22"""
print('Граф')
M, N = [int(x) for x in input().split()]
V = []
index = {}
A = [[0] * N for i in range(N)]
for i in range(N):
    v1, v2 = input().split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
            index[v] = len(V) - 1
        v1_i = index[v1]
        v2_i = index[v2]
print(index)

M, N = [int(x) for x in input().split()]
G = {}
for i in range(N):
    v1, v2 = input().split()
    for v, u in (v1, v2), (v2, v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)

