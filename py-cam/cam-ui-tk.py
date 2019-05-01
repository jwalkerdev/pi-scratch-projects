import tkinter as tk


class App:
    def __init__(self, master):
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
