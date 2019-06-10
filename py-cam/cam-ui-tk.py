import re
import tkinter as tk
import tkinter.messagebox as mb

'''
Methods to determine if the system is a raspberry pi
1)
import os
os.uname()[4][:3] == 'arm'
2) Read /proc/cpuinfo
https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py
'''

# Platform identification constants.
UNKNOWN          = 0
RASPBERRY_PI     = 1
BEAGLEBONE_BLACK = 2
MINNOWBOARD      = 3
JETSON_NANO      = 4

def pi_version():
    """
    Original source: https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py
    Detect the version of the Raspberry Pi.  Returns either 1, 2 or
    None depending on if it's a Raspberry Pi 1 (model A, B, A+, B+),
    Raspberry Pi 2 (model B+), or not a Raspberry Pi.
    """
    # Check /proc/cpuinfo for the Hardware field value.
    # 2708 is pi 1
    # 2709 is pi 2
    # 2835 is pi 3 on 4.9.x kernel
    # Anything else is not a pi.
    with open('/proc/cpuinfo', 'r') as infile:
        cpuinfo = infile.read()
    # Match a line like 'Hardware   : BCM2709'
    match = re.search('^Hardware\s+:\s+(\w+)$', cpuinfo,
                      flags=re.MULTILINE | re.IGNORECASE)
    if not match:
        # Couldn't find the hardware, assume it isn't a pi.
        return None
    if match.group(1) == 'BCM2708':
        # Pi 1
        return 1
    elif match.group(1) == 'BCM2709':
        # Pi 2
        return 2
    elif match.group(1) == 'BCM2835':
        # Pi 3 / Pi on 4.9.x kernel
        return 3
    else:
        # Something else, not a pi.
        return None


class App:
    pi_hw = False

    def __init__(self, master):
        # Determine if system is a raspberry pi
        hw_type = pi_version()
        self.pi_hw = True if hw_type is not None else False

        # Calculate dimensions
        max_width = master.winfo_screenwidth()
        max_height = master.winfo_screenheight()
        master.geometry("{}x{}+0+0".format(max_width-150, max_height-150))
        print("{}x{}+0+0".format(max_width-50, max_height-50))

        # Create primary frames
        frame_buttons = tk.Frame(master, 
                highlightbackground="blue", highlightcolor="blue", highlightthickness=2, bd=0)
        frame_buttons.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        frame_preview = tk.Frame(master, bg="black",
                highlightbackground="red", highlightcolor="red", highlightthickness=2, bd=0)
        frame_preview.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        # Create frame_buttons content
        tk.Label(frame_buttons, text='Cam Frame', highlightbackground="green", highlightcolor="red", highlightthickness=2, bd= 0).pack()
        tk.Button(frame_buttons, text='Start', command=self.start_preview).pack()
        tk.Button(frame_buttons, text='Stop', command=self.stop_preview).pack()

        # window expansion config
        master.rowconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        

    def start_preview(self):
        print('start_preview')
        if self.pi_hw:
            mb.showinfo("Pi Info","Message on Pi")
        else:
            mb.showinfo("Information","Informative message")
    
    def stop_preview(self):
        print('Not implemented - stop_preview')


# Create the main window
root_win = tk.Tk()
root_win.wm_title('PiCamera GUI')
#root_win.attributes('-fullscreen', True)

app = App(root_win)
root_win.mainloop()

# Run forever!
root_win.mainloop()
