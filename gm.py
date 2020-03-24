#!/usr/bin/python3
import time
import os
import threading


# FIELD SETTINGS
fsize = 15
field = []
for i in range(fsize ** 2):
    field.append(i)

# SNAKE SETTINGS
snake = [3,2,1,0]
slen = len(snake)
make = 1


def controller():
    global make
    while True:
        key = input()
        if key == 'w':
            make = -fsize
        elif key == 's':
            make = fsize
        elif key == 'a':
            make = -1
        elif key == 'd':
            make = 1


threading.Thread(target=controller).start()

# Main
while True:
    snake.pop(-1)
    snake.insert(0,snake[0]+make)
    for i in range (fsize ** 2):
        if i % fsize == 0:
            print('\n')
        if i in snake:
            if i == snake[0]:
                print('\033[35mS \033[0m', end='')
            else:
                print('\033[33mH \033[0m', end='')
        else:
            print('# ', end='')
    print('\n\033[32m', slen, '='*(15-len(str(slen))), '\033[0m')
    time.sleep(0.6)
    os.system('clear')


