from gpiozero import LED
from time import sleep
import threading

# GPIO17 : green wire  : LED1
# GPIO27 : orange wire : LED2
# GPIO22 : brown wire  : LED3

led1 = None
led2 = None
led3 = None
led_switcher = None
tb = None

class Mock_LED():
    def __init__(self):
        pass
    def on(self):
        pass
    def off(self):
        pass


def init():
    global led1, led2, led3, led_switcher, tb
    led1 = LED(17)
    led2 = LED(27)
    led3 = LED(22)
    led_switcher = {
        0: Mock_LED(),
        1: led1,
        2: led2,
        3: led3,
    }
    tb = 1.5   # time base

# Decorator: Makes a function run in its own thread
def worker_thread(func):
    def function_wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args,kwargs=kwargs)
        t.start()
    # Preserve primary original function properties
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper

def led_demo_1():
    led1.on()
    led2.on()
    led3.on()
    sleep(2)
    led1.off()
    sleep(1)
    led2.off()
    sleep(1)
    led3.off()

# led 0 is a rest (no led)
def play_note(id):
    target_led = led_switcher[id]
    target_led.on()
    sleep(0.25 * tb)
    target_led.off()

def play_note_list(note_list):
    for note in note_list:
        play_note(note)


def main():
    play_note_list(
        [2,2,2,1,
        2,2,2,1,
        2,1,2,3,
        2,2,2,2]
    )

init()

if __name__ == "__main__":
    main()
    exit(0)
