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
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = F[0]
    F[2] = F[1] + F[0]
    for i in range(3, n + 1):
        F[n] = F[n - 1] + F[n - 2] + F[n - 3]
    return F[n]
print(hopper(4))

print('Exercise 2. Grasshopper 2')


def hopper(n):
    """Determing grasshoppers task with 3 varieties of movement"""
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = F[0]
    F[2] = (F[1] + F[0]) * 3
    for i in range(3, n + 1):
        F[n] = F[n - 1] + F[n - 2] + F[n - 3]
    return F[n]
print(hopper(4))

print('Exercise 3. Grasshopper 3')


def count_min_cost(N, price: list):
    """
    Рассчитывает минимальную стоимость достижения точки
    N с минимальной price
    """
    c = [float('-inf'), price[1], price[1] + price[2]] + [0]*(N - 2)
    for i in range(3, N + 1):
        c[i] = price[i] + min(c[i - 1], c[i - 2])
    return c[N]


print(count_min_cost(5, [1, 1, 2, 2, 2, 1]))

print('Exercise 4. Grasshopper 4')


def count_min_cost(N, price: list):
    """
    Рассчитывает минимальную стоимость достижения точки
    N с минимальной price и определяет оптимальную траекторию
    """
    path = [0] * N
    c = [float('-inf'), price[1], price[1] + price[2]] + [0]*(N - 2)
    for i in range(3, N + 1):
        c[i] = price[i] + min(c[i - 1], c[i - 2])
        if c[i - 1] < c[i - 2]:
            path[i - 1] = price[i - 1]
        else:
            path[i - 1] = price[i - 2]
    print(path)
    return c[N]


print(count_min_cost(5, [1, 1, 2, 2, 2, 1]))

print('Exercise 5. Queen Game')


