"""MIPT Python Course Lections 17"""
print('Задача о рюкзаке')
m = [1, 2, 3, 5, 17]
v = [2, 4, 6, 2, 15]
N = len(m)
M = len(v)
F = [[0] * (N + 1) for i in range(M + 1)]
for i in range(1, N + 1):
    for k in range(1, M + 1):
        if m[i] <= k:
            F[k][i] = max(F[k][i - 1], v[i] + F[k - m[i]][i - 1])
        else:
            F[k][i] = F[k][i - 1]
