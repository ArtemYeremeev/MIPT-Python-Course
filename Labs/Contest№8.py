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
turtle.speed('fastest')

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def Koch_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    Koch_Curve(l, n - 1)
    turtle.left(60)
    Koch_Curve(l, n - 1)
    turtle.right(120)
    Koch_Curve(l, n - 1)
    turtle.left(60)
    Koch_Curve(l, n - 1)

Koch_Curve(400, 4)
turtle.reset()

print('Exercise 5. Kochs Snowflake')
turtle.speed('fastest')
Koch_Curve(400, 4)
turtle.right(120)
Koch_Curve(400, 4)
turtle.right(120)
Koch_Curve(400, 4)
turtle.reset()

print('Exercise 6. Minkovskys Curve')
turtle.speed('fastest')

def Minko_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 8
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)

Minko_Curve(3000, 3)
turtle.reset()

print('Exercise 7. Levys Curve')

turtle.speed('fastest')
def Levys_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 2
    Levys_Curve(l, n-1)
    turtle.right(90)
    Levys_Curve(l, n-1)
    turtle.left(90)
Levys_Curve(2000, 8)
turtle.reset()

print('Exercise 8. Dragons Curve')

turtle.speed('fastest')

def curve(l, n, direction = 45):
   if n == 0:
       turtle.forward(l)
       return
   turtle.right(direction)
   curve(l / 2, n - 1, 45)
   turtle.left(direction * 2)
   curve(l / 2, n - 1, - 45)
   turtle.right(direction)

L = 800
N = 5

curve(L, N)
turtle.reset()

print('Exercise 9. Cantor set')

def cantor_set(x, y, l, n):
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.forward(l)
        return

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.forward(l)

    cantor_set(x, y-30, l/3, n-1)
    cantor_set(x + l*2/3, y-30, l/3, n-1)

L = 400
N = 2
X = - L / 2
Y = 15 * N

turtle.penup()
turtle.goto(X, Y)
turtle.pendown()

cantor_set(X, Y, L, N)


