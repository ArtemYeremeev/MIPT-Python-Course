"""MIPT Python Course Lection 18"""
from collections import namedtuple
print('Именованный кортеж')
A = (1, 0, 3)
Point = namedtuple("Point", "x y z")
A = Point(1, 0, 3)
print("Значение точки А - ", A.x)
print("Расстояние до точки равно - ", A.x ** 2 + A.y ** 2 + A.z ** 2)

print('Связные списки')
a = [1]
a.append([2])
a[1].append([3, a])
p = a
while p is not None:
    print(p[0])
    p = p[1]


