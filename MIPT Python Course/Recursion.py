"""MIPT Python Course Lections 7-8"""
print('Факториал')
def f(n):
    assert n >= 0, 'Отрицательный факториал не определен'
    if n == 0:
        return 1
    return f(n - 1) * n
print(f(7))

print('Евклидовы отрезки')
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b,b)
    else:
        return gcd(a, b-a)
print(gcd(7,24))


print('Генерация всех перестановок')
def generate_number(N: int, M: int, prefix=None):
    """Генерирует все числа в N-ричной системе счисления (N <= 10) длины M"""
prefix = prefix or []
if M == 0:
    print(prefix)
for digit in range(N):
    prefix.append(digit)
    generate_number(N, M-1, prefix)
    prefix.pop()
generate_number(3,3)
