_stack = []


def push(x):
    _stack.append(x)


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return(len(_stack)) == 0


def output():
    list1 = []
    for x in range(len(_stack)):
        list1.append(_stack[x])
    return list1



