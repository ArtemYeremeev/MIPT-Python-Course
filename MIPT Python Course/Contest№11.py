"""MIPT Python Course Contest№11"""

print('Exercise 0. Fibonachi')
def fib(n):
    F = [-1]*(n+1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]
print(fib(13))

print('Exercise 1. Grasshopper 1')
def hopper(n):
    """Determing grasshoppers task with 3 varieties of movement"""
    F = [-1] * (n + 1)
    F[0] = 0
    F[1] = 1
    F[2] = 2
    F[3] = 3
    for i in range(4, n + 1):
        F[n] = F[n - 1] + F[n - 2] + F[n - 3]
    return F[n]
print(hopper(5))
