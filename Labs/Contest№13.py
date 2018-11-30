"""MIPT Python Course. Contest13"""
print('Exercise 1.')


def z_func(s):
    output = []
    if not s: return output
    i, slen = 1, len(s)
    output.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        output.append(left)
        i += 1
    return output


print(z_func('dasababadasdas'))

print('Exercise 2.')


def z_func_advanced(s1, s2):
    output = []
    if not s2 in s1: return output
    i, slen = 1, len(s1)
    output.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s2[left] == s2[right]:
            left += 1
            right += 1
        output.append(left)
        i += 1
    return output


s1 = input('Type string -')
s2 = input('Type substring -')
print(z_func_advanced(s1, s2))

print('Exercise 3.')


def prefix_func(s, n):
    pi = [0] * n
    for i in range(n - 1):
        for k in range(1, i + 1):
            equal = True
            for j in range(k):
                if s[j] != s[i - k  + 1 + j]:
                    equal = False
                    break
            if equal:
                pi[i] = k
    return pi


print(prefix_func(2, 1))