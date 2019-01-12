"""MIPT Python Course Lections 17"""
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