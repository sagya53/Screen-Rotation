import rotatescreen
import time
import win32api
screen = rotatescreen.get_primary_display()
for i in range(0):
    time.sleep(1)
    screen.rotate_to(i * 90 % 360)