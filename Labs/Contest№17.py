"""MIPT Python Course. Contest17"""
import matplotlib.pyplot as plt
import time


def get_pop_time(size, repeat_count, pop_position=None):
    '''
    size - размер списка из нулей на котором будем тестировать скорость операции pop
    repeat_count - количество повторений для усреднения
    pop_position - позиция с которой делаем pop
    '''
    l = [0] * size
    start_time = time.time()
    #
    # code here
    #
    end_time = time.time()
    return (end_time - start_time) / repeat_count


repeat_count = 1000
# code here
values1 = [get_pop_time(...) for size in range(10, 1000)]
values2 = [get_pop_time(...) for size in range(10, 1000)]
values3 = [get_pop_time(...) for size in range(10, 1000)]

plt.plot(values1, label='Pop no args')
plt.plot(values2, label='Pop start list')
plt.plot(values3, label='Pop end list')
plt.ylabel('pop time')
ax = plt.subplot(111)
ax.legend()
plt.show()