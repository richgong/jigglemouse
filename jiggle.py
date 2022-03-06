import time
from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)

while True:
    time.sleep(1.0)
    mouse.move(5, 5)
    time.sleep(1.0)
    mouse.move(-5, -5)
