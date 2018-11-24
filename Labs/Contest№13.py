"""MIPT Python Course. Contest13"""
print('Exercise 1.')


def z_func(s, n):
    n = len(s)
    z = [0] * n; left = right = 0
    for i in range(1, n):
        x = min(z[i - left], right - i + 1) if i <= right else 0
        while 1 + x < n and s[x] == s[i + x]:
            x += 1
        z[i] = x
        if i + x - 1 > right:
            left, right = i, i + x - 1
    return z


z_func('abcab', 2)