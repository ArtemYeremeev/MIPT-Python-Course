"""MIPT Python Course. Contest14"""
from random import randint
from lib import _stack

print('Exercise 1. Stack')

print('Стек пуст?', _stack.is_empty())

for x in range(5):
    _stack.push(randint(1, 10))
print('В стеке находятся следующие числа', _stack.output())
for x in range(5):
    print('Достаю верхний элемент стека - ', _stack.pop())

print('Стек пуст?', _stack.is_empty())


print('Exercise 2. Bracers structures ')

bracers = input('Введите скобочную последовательность - ')


def check_bracers_sequence(bracers):
    """Проверяет корректность скобочной последовательности"""
    for brace in bracers:
        if brace not in "{}[]":
            continue
        if brace in '{[':
            _stack.push(brace)
        else:
            if _stack.is_empty():
                return False
            left = _stack.pop()
            if left == '{':
                right = '}'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return _stack.is_empty()


check_bracers_sequence(bracers)

print('Exercise 3. Reversive Polish notation')

ints = str(list(range(0, 11)))
bracers = ['(', ')']
operands = ['+', '-', '*', '/']
x = list('(3+4*(2-1))/5')
print('Выражение получено - ', x)
for i in range(len(x)):
    if x[i] in bracers:
        pass
    if x[i] in ints:
        _stack.push(x[i])
    if x[i] in operands:
        _stack.push(x[i])
print('Реверсирование выполнено - ', _stack.output())


