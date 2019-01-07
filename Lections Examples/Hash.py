"""MIPT Python Course Lections 17"""
print('Хеш')


def calc_hash(data):
    k = 3571
    s = 0
    i = 1
    data += 84832541
    while data > 0:
        s += data % 2 * k ** i
        i += 1
        data //= 2
    return s % 2 ** 32
