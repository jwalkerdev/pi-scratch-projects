import tkinter as tk

# Re-write this UI to show and manipulate GPIO pins

'''
UI for working with GPIO pins
Project Stage
    1. Static pin map
    2. Read the pin map from the system (based on pinout rpi os command)
Features Ideas
    - Buttons next to each GPIO
    - Listen with interrupts where possible
    - Give option to send data sets to thingify based on time and/or change


Physical Pin Numbering Pattern
    1   2
    3   4
    ...

40-pin RPI 3B+ GPIO pinout

40-pin RPI B+, 2, 3, and Zero GPIO pinout:
   3V3  (1) (2) 5V
 GPIO2  (3) (4) 5V
 GPIO3  (5) (6) GND
 GPIO4  (7) (8) GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8
   GND (25) (26) GPIO7
 GPIO0 (27) (28) GPIO1
 GPIO5 (29) (30) GND
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

More detailed table for RPI B+, 2, 3, and Zero GPIO pinout:
Alt Fn          |                              | Alt Fn
                | 3V3 PWR |  1 || 2  | 5V PWR |
I2C_SDA1        | BCM2    |  3 || 4  | 5V PWR |
I2C_SCL1        | BCM3    |  5 || 6  |    GND |
GPCLK0          | BCM4    |  7 || 8  |  BCM14 | UART0_TXD
                | GND     |  9 || 10 |  BCM15 | UART0_RXD
SPI1_CE1        | BCM17   | 11 || 12 |  BCM18 | PWM0, PCM_CLK
                | BCM27   | 13 || 14 |    GND |
                | BCM22   | 15 || 16 |  BCM23 |
                | 3V3 PWR | 17 || 18 |  BCM24 |
SPI0_MOSI       | BCM10   | 19 || 20 |    GND | 
SPI0_MISO       | BCM9    | 21 || 22 |  BCM25 | 
SPI0_SCLK       | BCM11   | 23 || 24 |   BCM8 | SPI0_CE0
                | GND     | 25 || 26 |   BCM7 | SPI0_CE1
I2C_SDA1, ID_SD | BCM0    | 27 || 28 |   BCM1 | I2C_SCL0, ID_SC
GPCLK1          | BCM5    | 29 || 30 |    GND | 
GPCLK2          | BCM6    | 31 || 32 |  BCM12 | PWM0
PWM1            | BCM13   | 33 || 34 |    GND |
SPI1_MISO, PWM1 | BCM19   | 35 || 36 |  BCM16 | SPI1_CE2
                | BCM26   | 37 || 38 |  BCM20 | SPI1_MOSI
                | GND     | 39 || 40 |  BCM21 | SPI1_SCLK

---------------------------------

Static pin mapping to buttons
Using the following pins:
    (36) GPIO16
    (38) GPIO20
    (40) GPIO21
   '''



class App:
    def __init__(self, master):
        # Calculate dimensions
        max_width = master.winfo_screenwidth()
        max_height = master.winfo_screenheight()
        master.geometry("{}x{}+50+50".format(max_width-150, max_height-150))
        print("{}x{}+50+50".format(max_width-50, max_height-50))

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
        print('Not implemented - start_preview')
    
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


'''
from Tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)

mainloop()
'''
