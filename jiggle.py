import random
import time
from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position

# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)

base = 100

while True:
    rand = random.random() * 1.0
    print(rand)
    print(f'Current position: {int(mouse.position[0])} {int(mouse.position[1])} rand={rand}')
    mouse.position = (549, 637)
    mouse.click(Button.left, 1)
    time.sleep(rand * 2.0 + 1.0)
    mouse.position = (1214, 637)
    mouse.click(Button.left, 1)
    time.sleep(rand)
    mouse.move(base * rand, base * rand)
    time.sleep(rand)
    mouse.move(-base * rand, -base * rand)
