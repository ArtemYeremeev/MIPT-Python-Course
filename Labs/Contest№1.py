"""MIPT Python Course. Contest1"""
import turtle
print('Упражнение 1. Гипотенуза')
a = 179
b = 197
c = (a**2+b**2)**0.5
print(c)
print('Выполнено')

print('Упражнение 2. Буква S')
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.reset()
print('Выполнено')

print('Упражнение 3. Квадрат')
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.reset()
print('Выполнено')

print('Упражнение 4. Окружность')
x = 120
while x > 0:
    turtle.left(3)
    turtle.forward(5)
    x -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 5. Вложенные квадраты')
turtle.left(90)
b = 10
c = 5
a = 200
while b > 0:
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)

    turtle.penup()
    turtle.forward(c)
    turtle.right(90)
    turtle.forward(c)
    turtle.pendown()
    turtle.left(90)
    a -= 10
    b -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 6. Паук')
n = 12
u = 360/n
k = n
while k > 0:
    turtle.right(u)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(90)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    k -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 7. Архимедова спираль')
f = 3
a = 1
t = 400
while t >= 0:
    p = (a * f) / (2 * 3.14)
    turtle.left(f)
    turtle.forward(p)
    a = a+0.1
    t -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 8. Квадратная спираль')
t = 15
a = 30
while t >= 0:
    turtle.forward(a)
    turtle.left(90)
    a += 30
    t -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 9. Правильные многоугольники')
n = 6
f = 360/n
t = n
c = 5
d = 60
for y in range(10):
    for x in range(n):
        turtle.left(f)
        turtle.forward(d)
        t -= 1
    d -= 5
    turtle.penup()
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(2.5)
    turtle.right(180)
    turtle.pendown()
turtle.reset()
print('Выполнено')

print('Упражнение 10. Цветок')
for x in range(5):#5 лепестков
    turtle.circle(45)
    turtle.penup()
    turtle.left(360/5)#5 лепестков
    turtle.forward(45)
    turtle.pendown()
turtle.reset()
print('Выполнено')

print('Упражнение 11. Бабочка')
turtle.circle(40)
turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.circle(40)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.forward(110)
turtle.pendown()
turtle.circle(50)
turtle.left(90)
turtle.penup()
turtle.forward(240)
turtle.pendown()
turtle.left(90)
turtle.circle(50)
turtle.penup()
turtle.forward(40)
turtle.left(90)
turtle.forward(120)
turtle.pendown()
turtle.circle(25)
turtle.reset()
print('Выполнено')

print('Упражение 12. Пружина')
n = 120
f = 360/n
t = n
c = 5
d = 5
for y in range(10):
    for x in range(n):
        turtle.left(f)
        turtle.forward(d)
        t -= 1
    d -= 0.5
    turtle.penup()
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(2.5)
    turtle.right(180)
    turtle.pendown()
turtle.reset()
print('Выполнено')

print('Упражнение 13. Смайл')
turtle.circle(100)
turtle.penup()
turtle.forward(55)
turtle.left(90)
turtle.forward(130)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.left(90)
turtle.forward(80)
turtle.pendown()
turtle.right(90)
turtle.circle(20)
turtle.right(180)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.left(90)
turtle.right(45)
x = 20
while x > 0:
    turtle.left(5)
    turtle.forward(3)
    x -= 1
turtle.reset()
print('Выполнено')

print('Упражнение 14. Звезды')
n = 5
for x in range(n):
    turtle.left(720/n)
    turtle.forward(120)
turtle.reset()
n = 11
for y in range(n):
    turtle.left(720/n)
    turtle.forward(120)
turtle.reset()
print('Выполнено')
