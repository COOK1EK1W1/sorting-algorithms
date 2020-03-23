import random
import ezgui

width, height = 600, 650

screen = ezgui.Screen(width, height)

items = [i for i in range(width)]
random.shuffle(items)

for i, point in enumerate(items):
    screen.rect(i, point , 1, width - point)

def randomize():
    global items
    random.shuffle(items)
    screen.rect(0, 0, width, width, (255,255,255))
    for i, point in enumerate(items):
        screen.rect(i, point , 1, width - point)

def solve1():
    global items, screen, width, height
    for j in range(len(items) - 1):
        for i in range(len(items) - j - 1):

            if items[i] < items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
                screen.rect(i, 0, 2, width, (255,255,255))
                screen.rect(i, items[i] , 1, width - items[i])
                screen.rect(i + 1, items[i + 1] , 1, width - items[i + 1])

screen.add_button(0, width, 50, 50, func=randomize, colour=(255, 0, 0))
screen.add_button(50, width, 50, 50, func=solve1, colour=(0, 255, 0))

screen.run()
