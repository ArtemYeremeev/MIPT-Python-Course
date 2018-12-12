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


print('Exercise 3. Polish notation')

ints = str(list(range(0, 11)))
operators = ['+', '-', '*', '/']
numeras = list(range(0, 10))
x_reversive = list('34+21-*5/')
x_direct = list('*+34-21/5')

x = x_reversive
print('Reversive input -', x)
for i in range(len(x_reversive)):
    result = x[i]
    if x[i] in numeras:
        int(_stack.push(x[i]))
    if x[i] in operators:
        num1 = int(_stack.pop())
        num2 = int(_stack.pop())
        if x[i] == '+':
            result = (num1 + num2)
        if x[i] == '-':
            result = (num2 - num1)
        if x[i] == '*':
            result = (num1 * num2)
        if x[i] == '/':
            result = (num2 / num1)
    _stack.push(result)
    print(_stack.output())

print('Exercise 4. Stack calculator')

expression = list(input('Введите ваше мат. выражение - '))

operators = ['+', '-', '*', '/']
numeras = str(list(range(0, 10)))

list1 = []
list2 = []
list3 = []

for x in range(len(expression)):
    if expression[x] in numeras:
        list1.append(expression[x])
    if expression[x] in operators:
        list2.append(expression[x])

print(list1)
print(list2)

for x in range(len(expression)):
    if list2[0] == '+':
        if list1[x] and list1[x + 1] in numeras:
            print(list1[x] + list1[x+1])


