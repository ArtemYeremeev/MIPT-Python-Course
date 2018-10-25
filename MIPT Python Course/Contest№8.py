"""MIPT Python Course Contest 8"""
import sys
print('Exercise 1. Factorial')


def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


print(fac(10))

print('Exercise 2. Recursion depth')


def endless_recursion():
    endless_recursion()

try:
    endless_recursion()
except:
    print("Stack Overflow", sys.getrecursionlimit())


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print('Exercise 3. Fibonacci numbers')


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(7))

print('Exercise 4. Kochs Curve ')

import turtle

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def Koch_Line(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)
    turtle.right(120)
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)


Koch_Line(400, 4)