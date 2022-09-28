# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pynput.mouse import Controller
import random
import time
import tkinter

root = tkinter.Tk()
root.withdraw()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
mouse = Controller()


def print_hi():
    for x in range(1, 1800):
        # Set pointer position
        mouse.position = (10, 20)
        print('Time {0} seg'.format(x * 2))

        # Move pointer relative to current position
        mouse.move(random.randint(0, WIDTH), random.randint(0, HEIGHT))

        # Press and release
        #mouse.press(Button.left)
        #mouse.release(Button.left)
        time.sleep(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# https://code.visualstudio.com/docs/python/python-tutorial