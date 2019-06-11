from time import sleep
import re
import tkinter as tk
import tkinter.messagebox as mb
from picamera import PiCamera
import signal

# if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
#     from Tkinter import *
# else:
#     from tkinter import *

'''
Methods to determine if the system is a raspberry pi
1)
import os
os.uname()[4][:3] == 'arm'
2) Read /proc/cpuinfo
https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py


TK Menu notes:
If you want to hide a menu, too, there are only two ways I've found to do that. One is to destroy it. The other is to make a blank menu to switch between.
self.tk.config(menu=self.blank_menu)  # self.blank_menu is a Menu object

Then switch it back to your menu when you want it to show up again.
self.tk.config(menu=self.menu)  # self.menu is your menu.

'''

##################### ADAFRUIT GPIO CODE - START #####################

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

##################### ADAFRUIT GPIO CODE - END #####################


class App:
    pi_hw = False
    camera = None

    def __init__(self, master):
        # Store master window
        self.master = master
        # Determine if system is a raspberry pi
        hw_type = pi_version()
        self.pi_hw = True if hw_type is not None else False

        # Calculate dimensions
        max_width = master.winfo_screenwidth()
        max_height = master.winfo_screenheight()
        print("Screen size: {}x{}", max_width, max_height)
        # master.geometry("{}x{}+0+0".format(max_width-10, max_height-10))
        # print("{}x{}+0+0".format(max_width-50, max_height-50))

        # Maximize the window. Not directly related to fullscreen mode
        master.attributes('-zoomed', True)
        # Setup fullscreen state and binding to toggle
        self.fullscreen_state = True
        master.attributes("-fullscreen", True)
        master.bind("<Escape>", self.toggle_fullscreen)

        # Create primary frames
        frame_buttons = tk.Frame(master, 
                highlightbackground="blue", highlightcolor="blue", highlightthickness=2, bd=0)
        frame_buttons.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        frame_preview = tk.Frame(master, bg="black",
                highlightbackground="red", highlightcolor="red", highlightthickness=2, bd=0)
        frame_preview.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        # Create frame_buttons content
        tk.Label(frame_buttons, text='Cam Frame', highlightbackground="green", highlightcolor="red", highlightthickness=2, bd= 0).pack()
        tk.Button(frame_buttons, text='Start', command=self.show_cam_preview).pack()
        tk.Button(frame_buttons, text='Stop', command=self.hide_cam_preview).pack()

        # window expansion config
        master.rowconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

    def toggle_fullscreen(self, event=None):
        self.fullscreen_state = not self.fullscreen_state
        self.master.attributes("-fullscreen", self.fullscreen_state)

    def show_cam_preview(self):
        print('start_preview')
        if self.pi_hw:
            mb.showinfo("Pi Info","Message on Pi")
            self.test_camera_usage_01()
        else:
            mb.showinfo("Information","Informative message")
    
    def hide_cam_preview(self):
        print('Not implemented - stop_preview')

    def test_camera_usage_01(self):
        # 4:3 resolutions
        res_qvga = (320,240)
        res_hvga = (480,320)
        res_vga  = (640,480)
        res_svga = (800,600)
        res_xga = (1024,768)
        res_pal = (768,576)
        # 3:2 resolutions
        res_480p = (720,480)  # DVD
        # 16:9 resolutions
        res_720p = (1280,720)
        res_1080p = (1920,1080)
        res_ultrahd_4k = (3840,2160)
        res_ntsc = (640,360) # nHD
        res_hdtv = (1280,720) # wxga

        cam_res = res_xga
        
        camera = PiCamera()
        camera.resolution = cam_res
        camera.framerate = 30 # Frame rate
        camera.exposure_mode = 'auto'  # off,auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
        camera.vflip = True    # Vertical Flip the video from the camera
        camera.hflip = True    # Horizontal Flip the video from the camera
         # Set preview window location and size. preview_window attr is deprecated but still in use
        if hasattr(camera, 'preview_window'):
            camera.preview_fullscreen = False
            camera.preview_window = (20,20,400,300)
        else:
            camera.fullscreen = False
            camera.window = (20,20,400,300)
        camera.start_preview()
        sleep(3)
        camera.stop_preview()
        camera.close()

        # camera.__slots__  # to see attributes of the camera object


# def sigint_handler(signum, frame):
#     print('CTRL+C/SIGINT received!')
 
# signal.signal(signal.SIGINT, sigint_handler)

# def toggle_fullscreen(window, event=None):
#     #self.state = not self.state     # Just toggling the boolean
#     #self.tk.attributes("-fullscreen", self.state)
#     window.attributes("-fullscreen", True)
#     return "break"

def end_fullscreen(window, event=None):
    #self.state = False
    window.attributes("-fullscreen", False)
    return "break"

# Create the main window
root_win = tk.Tk()
root_win.wm_title('PiCamera GUI')
root_win.attributes('-fullscreen', True)
root_win.bind("<Escape>", end_fullscreen(root_win))

app = App(root_win)
root_win.mainloop()

# Run forever!
root_win.mainloop()



### Doc
'''
https://en.wikipedia.org/wiki/Graphics_display_resolution

Resolution Info:
DVD: 720x480
QVGA: 320x240
720p: 1280x720
1080p: 1920x1080
Ultra HD(4k): 3840x2160
NTSC: 640x360 (16/9)
PAL: 720x405 (16/9)
HDTV: 1280x720

4:3 ratios
HVGA: 480x320
VGA:  640x480
SVGA: 800x600
XGA:  1024x768

https://picamera.readthedocs.io/en/release-1.12/fov.html
- Camera V2 Supported Modes
#	Resolution	Aspect Ratio	Framerates	Video	Image	FoV	    Binning
1	1920x1080	    16:9	    0.1-30fps	x	     	    Partial	None
2	3280x2464	    4:3	        0.1-15fps	x	    x	    Full	None
3	3280x2464	    4:3	        0.1-15fps	x	    x	    Full	None
4	1640x1232	    4:3 	    0.1-40fps	x	     	    Full	2x2
5	1640x922	    16:9	    0.1-40fps	x	     	    Full	2x2
6	1280x720	    16:9	    40-90fps	x	     	    Partial	2x2
7	640x480	        4:3	        40-90fps	x	     	    Partial	2x2
- Camera V1 Supported Modes
#	Resolution	Aspect Ratio	Framerates	Video	Image	FoV	    Binning
1	1920x1080	    16:9	    1-30fps	    x	     	    Partial	None
2	2592x1944	    4:3	        1-15fps	    x	    x	    Full	None
3	2592x1944	    4:3	        0.1666-1fps	x	    x	    Full	None
4	1296x972	    4:3	        1-42fps	    x	     	    Full	2x2
5	1296x730	    16:9	    1-49fps 	x	     	    Full	2x2
6	640x480	        4:3	        42.1-60fps	x	     	    Full	4x4
7	640x480	        4:3	        60.1-90fps	x	     	    Full	4x4

Parts Used:
    - LCD
        - Velleman VMP400 320x480 SPI LCD
        - interfaces with rpi gpio ports
    - Camera
        - smraza: Camera Module for Raspberry Pi 3 with 5MP 1080p OV5647 Video Webcam
            - https://www.amazon.com/gp/product/B073183KYK
            - Supports Night Vision Compatible with Raspberry Pi 3b 2 Model B B+
            - Image resolution:  1080p / 1920x1080
                - Scale ratio to 480x320:   4x3.375
                - Scaled resolutions:
                    - 1440x960 (3x)
                    - 1620x1080 (3.375x)
            - Video modes
                1080p30 (1920x1080 @ 30 fps)
                720p60 (1280x720 @ 60 fps)
                640 x 480p60/90
'''
