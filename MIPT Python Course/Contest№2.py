import robot
r = robot.rmap()
r.sleep=0.5
print('Упражнение 1.1')#1
r.lm('task1-1')
r.rt(2)
r.down(1)
print('Выполнено')

print('Упражнение 1.2')#2
r.lm('task1-2')
r.rt(2)
r.down(2)
r.pt()
r.down(1)
r.rt(2)
print('Выполнено')

print('Упражнение 3.1')#3
r.lm('task3-1')
while r.fr():
    r.rt(1)
print('Выполнено')

print('Упражнение 3.3')#4
r.lm('task3-3')
while not r.isPark():
    if r.fr():
        r.rt(1)
    else:
        if r.fl():
            r.lt(1)
        else:
            if r.fu():
                r.up(1)
            else:
                if r.fd():
                    r.dn(1)

print('Выполнено')

print('Упражнение 5.2')#5
r.lm('task5-2')
while not r.isPark():
    r.rt(1)
print('Выполнено')

print('Упражнение 5.3')#6
r.lm('task5-3')
while not r.isPark():
    r.rt(1)
print('Выполнено')

print('Упражнение 5.4')#7
r.sleep=0.15
r.lm('task5-4')
r.rt(18)
r.dn(16)
r.lt(18)
while not r.isPark():
    r.up(1)
print('Выполнено')

print('Упражнение 5.7')#8
r.lm('task5-7')
while not r.isPark():
    r.rt(1)
print('Выполнено')

print('Упражнение 8.2')#9
r.lm('task8-2')
for step1 in range(33):
    if r.wu():
        r.rt(1)
    else:
        r.pt()
        r.rt(1)
print('Выполнено')

print('Упражнение 8.3')#10
r.lm('task8-3')
for step2 in range(33):
    if r.wu():
        r.pt()
        r.rt(1)
    else:
        if r.wd():
            r.pt()
            r.rt(1)
        else:
            r.rt(1)
print('Выполнено')

print('Упражнение 8.4')#11
r.lm('task8-4')
for step3 in range(33):
    if all([r.wu(), (r.wd())]):
        r.pt()
        r.rt(1)
    else:
        r.rt(1)
print('Выполнено')

print('Упражнение 8.6')#12
r.lm('task8-6')
print('Упражнение 8.6')#12
r.lm('task8-6')
for ras in range(33):
    if all([not r.wu(), (r.wd())]):
        r.pt()
        r.rt(1)
    else:
        r.rt(1)
print('Выполнено')

print('Упражнение 8.10')#13
r.lm('task8-10')
for step5 in range(33):
    if not r.wd():
        r.dn(1)
        r.pt()
        r.up(1)
    if not r.wu():
        r.up(1)
        r.pt()
        r.dn(1)
        r.rt(1)
    else:
        r.rt(1)
print('Выполнено')

print('Упражнение 8.11')#14
r.lm('task8-11')
while not r.isPark():
    if all([r.wu(), (r.wd())]):
        r.pt()
    if not r.wd():
        r.dn(1)
        r.pt()
        r.up(1)
    if not r.wu():
        r.up(1)
        r.pt()
        r.dn(1)
        r.rt(1)
    else:
        r.rt(1)
print('Выполнено')

print('Упражнение 8.21')#15
r.lm('task8-21')
if r.wr():
    r.lt(8)
else:
    r.rt(8)
if r.wu():
    r.dn(8)
else:
    r.up(8)
print('Выполнено')

print('Упражнение 8.22')#16
r.lm('task8-22')
while not r.isPark():
    if not r.wu():
        r.up(1)
    if not r.wr():
        while not r.isPark():
            r.rt(1)
    if not r.wl():
        while not r.isPark():
            r.lt()
print('Выполнено')

print('Упражнение 8.27')#17
r.lm('task8-27')
while not r.cl():
    r.up()
if r.cl():
    r.rt(1)
while not r.cl():
    r.rt(1)
    if r.wr():
        while not r.cl():
            r.lt(1)
        if r.cl():
            r.lt(1)
            while not r.cl():
                r.lt(1)
print('Выполнено')

print('Упражнение 8.28')#18
r.lm('task8-28')
print('Выхожу на исходную')
while not r.wl():
    r.lt(1)
print('Ищу путь сверху')
while not r.isPark():
    if not r.wr():
        if r.wu():
            r.rt(1)
        if not r.wu():
            while not r.wu():
                r.up(1)
            if r.wu():
                while not r.wl():
                    r.lt(1)
                else:
                    break
    else:
        break
print('Ищу путь снизу')
while not r.wl():
    while r.wd():
        r.lt(1)
    else:
        r.dn(1)
        while not r.wl():
            r.lt(1)
        else:
            while not r.wu():
                r.up(1)
print('Выполнено')

print('Упражнение 8.29')#19
r.lm('task8-29')
print('Выхожу на исходную')
while not r.wl():
    r.lt(1)
print('Ищу путь сверху')
while not r.isPark():
    if not r.wr():
        if r.wu():
            r.rt(1)
        if not r.wu():
            while not r.wu():
                r.up(1)
            if r.wu():
                while not r.wl():
                    r.lt(1)
                else:
                    break
    else:
        break
print('Ищу путь снизу')
while not r.isPark():
    if not r.wl():
        while r.wd():
            r.lt(1)
        else:
            r.dn(1)
            while not r.wl():
                r.lt(1)
            else:
                while not r.wu():
                    r.up(1)
    else:
        while r.wr():
            r.rt(1)
print('Выполнено')

print('Упражнение 4.3')#20
r.lm('task4-3')
print('Выхожу на исходную')
r.rt(1)
print('Начинаю окрашивание')
for y in range(6):
    for x1 in range(27):
        r.pt()
        r.rt(1)
    print('Разворот')
    r.dn(1)
    r.lt(1)
    for x2 in range(27):
        r.pt()
        r.lt(1)
    print('Разворот')
    r.dn(1)
    r.rt(1)
print('Иду на парковку')
print('Выполнено')

print('Упражнение 4.11')#21
r.lm('task4-11')
r.sleep=0.1
r.rt(1)
for q in range(1,15):
    for z in range(1,q):
        r.pt('red')
        r.rt(1)
    r.lt(q-1)
    r.dn(1)
print('Выполнено')


print('Упражнение 5.10')#22
r.lm('task5-10')
print('Рассчитываю размер поля')
dlina=0
shirina=0
while not r.wr():
    r.rt(1)
    shirina+=1
if r.wr():
    r.lt(shirina)
while not r.wd():
    r.dn(1)
    dlina+=1
if r.wd():
    r.up(dlina)
print('Начинаю окрашивание')
for d in range(dlina+1):
    while not r.wr():
        r.pt()
        r.rt(1)
    if r.wr():
        r.pt()
        print('Разворот')
        if not r.wd():
            r.dn(1)
        while not r.wl():
            r.lt(1)
print('Иду на парковку')
while not r.wl():
    r.rt(1)
print('Выполнено')

print('Упражнение 6.6')#23
r.lm('task6-6')
shag=0
print('Иду по коридору, считаю шаги')
while not r.wr():
    r.rt(1)
    shag+=1
if r.wr():
    print('Число шагов равно',shag)
    print('Разворот, начинаю обход')
for w in range(shag):
    if not r.wu():
        print("Найден новый коридор")
        r.up(1)
        while not r.wu():
            r.pt()
            r.up(1)
        if r.wu():
            r.pt()
            while not r.wd():
                r.dn(1)
            if r.wd():
                r.lt(1)
    else:
        r.lt(1)
print('Выполнено')

print('Упражнение 2.1')#24
r.lm('task2-1')
print('Начинаю окрашивание')
r.rt(2)
for v1 in range(3):
    r.dn(1)
    r.pt()
r.rt(1)
r.up(1)
for v2 in range(3):
    r.pt()
    r.lt(1)
print('Иду на парковку')
r.rt(1)
r.up(1)
print('Выполнено')

r.lm('task2-2')
print('Начинаю окрашивание')
for cycle in range(5):
    r.rt(1)
    for v8 in range(3):
        r.dn(1)
        r.pt()
    r.rt(1)
    r.up(1)
    for v9 in range(2):
        r.pt()
        r.lt(1)
    r.pt()
    for v3 in range(4):
        if not r.wr():
            r.rt(1)
    r.up(2)
    print('Иду на следующее поле')
r.lt(2)
r.dn(1)
print('Выполнено')

print('Упражнение 2.4')#26
r.lm('task2-4')
print('Начинаю окрашивание')
for cycle1 in range(4):
    for cycle2 in range(10):
        r.rt(1)
        for v4 in range(3):
            r.pt()
            r.dn(1)
        r.rt(1)
        r.up(2)
        for v5 in range(2):
            r.pt()
            r.lt(1)
        r.pt()
        for v6 in range(4):
            if not r.wr():
                r.rt(1)
        r.up(1)
    print('Иду на исходную')
    r.lt(38)
    for p in range(4):
        if not r.wd():
            r.dn(1)
for cycle13 in range(10):
    r.rt(1)
    for cycle15 in range(2):
        r.pt()
        r.dn(1)
    r.pt()
    r.rt(1)
    r.up(1)
    for cycle18 in range(2):
        r.pt()
        r.lt(1)
    r.pt()
    r.up(1)
    for x13 in range(4):
        if not r.wr():
            r.rt(1)
r.lt(38)
print('Выполнено')

print('Упражнение 7.5')#27
r.lm('task7-5')
yolo=0
while not r.wr():
    zamer=0
    print(zamer)
    while not r.wr():
        r.rt(1)
        zamer+=1
    if not r.wl():
        r.lt(zamer)
    if zamer>=yolo:
            r.pt()
            r.rt(yolo)
            yolo+=1
    else:
        r.pt()
        while not r.wr():
            r.rt(1)
print('Выполнено')

print('Упражнение 7.6')#28
r.lm('task7-6')
for x20 in range(5):
    while not r.cl():
        r.rt(1)
    else:
        r.rt(1)
r.lt(1)
print('Выполнено')

print('Упражнение 7.7')#29
r.lm('task7-7')
while not r.cl():
    r.rt(1)
    if r.cl():
        r.rt(1)
        if r.cl():
            r.rt(1)
            if r.cl():
                print('Бинго')
                r.rt(1)
                break
r.lt(1)
print('Выполнено')

print('Упражнение 9.3')#30
r.lm('task9-3')
print('Крашу синее поле')
d=17
w=9
for paint0 in range(w):
    for paint1 in range(d):
        r.rt(1)
        r.pt('Blue')
    r.lt(d)
    d-=2
    print('Разворот')
    r.dn(1)
    r.rt(1)
r.lt(1)
r.dn(1)
print('Крашу желтое поле')
d=1
w=9
for paint3 in range(w-1):
    for paint4 in range(d):
        r.rt(1)
        r.pt('Yellow')
    r.lt(d)
    d+=2
    print('Разворот')
    if not r.wd():
        r.dn(1)
        r.lt(1)
    else:
        r.rt(1)
        r.up(1)
for paint5 in range(17):
    r.rt(1)
    r.pt('Yellow')
r.lt(17)
print('Крашу красное поле')
d=9
w=17
for paint6 in range(d):
    for paint7 in range(w):
        r.up(1)
        r.pt('Red')
    r.dn(w)
    w-=2
    print('Разворот')
    r.up(1)
    r.rt(1)
r.rt(1)
r.dn(1)
print('Крашу зеленое поле')
d=9
w=1
for paint8 in range(d):
    for paint9 in range(w):
        r.up(1)
        r.pt()
    r.dn(w)
    w+=2
    print('Разворот')
    r.dn(1)
    r.rt(1)
print('Иду на парковку')
while not r.wl():
    r.lt(1)
print('Выполнено')

print('Упражнение 8.30')#31
r.lm('task8-30')
for komnata in range(100):
    if r.isPark():
        break
    while not r.wr():
        r.rt(1)
    while not r.wd():
        r.dn(1)
    while r.wd():
        r.lt(1)
        if not r.wd():
            r.dn(1)
            break
        if all([r.wl(), (r.wd())]):
            break
print('Выполнено')

print('Упражнение 8.18')#32
r.lm('task8-18')
pyatna=0
shag1=0
print('Иду по коридору, считаю шаги')
while not r.wr():
    r.rt(1)
    shag1+=1
if r.wr():
    print('Число шагов равно',shag1)
    print('Разворот, иду на старт')
r.lt(shag1)
for w1 in range(shag1):
    if not r.wu():
        print("Найден новый коридор")
        r.up(1)
        if r.cl():
            pyatna += 1
            print('Обнаружено пятно')
        while not r.wu():
            if r.cl():
                pyatna+=1
                print('Обнаружено пятно')
            r.up(1)
        if r.wu():
            while not r.wd():
                r.dn(1)
            if r.wd():
                if r.label():
                    r.pt()
                    pyatna += 1
                    print('Обнаружено пятно')
                r.rt(1)
    else:
        r.rt(1)
print('Число пятен -',pyatna)
print('Выполнено')
