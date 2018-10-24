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
print(sys.getrecursionlimit())
def endless_recursion():
    endless_recursion()

print('Exercise 3. Fibonacci numbers')
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(7))

