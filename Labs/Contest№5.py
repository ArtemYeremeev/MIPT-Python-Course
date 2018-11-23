"""MIPT Python Course. Contest5"""
from lib import graphics as gr

print('1. Движение шара')
SIZE_X = 400
SIZE_Y = 400
# Исходные данные
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
coords = gr.Point(200, 200)
velocity = gr.Point(2, 0)


def add(point_1, point_2):
    """Функция, описывающая изменение положения шара"""
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


def clear_window():
    """Функция, очищающая поле"""
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def wall(coords, velocity):
    """Функция, проверяющая контакт мяча со стеной"""
    if coords.x < 15 or coords.x > SIZE_X - 15:
        velocity.x = -velocity.x
    if coords.y < 15 or coords.y > SIZE_Y - 15:
        velocity.y = -velocity.y


def draw_ball(coords):
    """Функция визуализации"""
    circle = gr.Circle(coords, 15)
    circle.setFill('yellow')
    circle.draw(window)


for t in range(150):
    clear_window()
    draw_ball(coords)
    wall(coords, velocity)
    coords = add(coords, velocity)
    gr.time.sleep(0.02)
    t -= 1

window.getMouse()
window.close()

print('2. Скачущий мяч')
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)
velocity = gr.Point(5, 2)
acceleration = gr.Point(0, 0.1)


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


for t in range(300):
    clear_window()
    draw_ball(coords)
    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    wall(coords, velocity)
    gr.time.sleep(0.02)
    t -= 1

window.getMouse()
window.close()
