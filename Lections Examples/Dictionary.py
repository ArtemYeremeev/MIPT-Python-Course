"""MIPT Python Course Lection 21"""
print('Словарь')

votes = {}
N = int(input())
for i in range(N):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

