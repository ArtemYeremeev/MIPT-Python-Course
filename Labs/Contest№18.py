"""MIPT Python Course. Contest14"""


def move(me, enemies, bullets, bonuses, m):
    if me['pos'][1] < 500:
        m.down()

    m.shot(400, 300)
