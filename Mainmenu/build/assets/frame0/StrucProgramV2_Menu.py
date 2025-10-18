import os
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from PIL import Image, ImageTk, ImageSequence
import threading
import time


# Create the main window
window = tk.Tk()
window.title("XSTRUCT PRO ENHANCE v2")
window.geometry("800x500")
window.configure(bg="#006AEC")

# Center the main window on the screen
window_width = 800
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
window.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

# Load the icon image
icon_image = Image.open("xstruclogo.jpg")
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(False, icon_photo)

# Create a canvas
canvas = Canvas(
    window,
    bg="#006AEC",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load and create image elements (keep references)
image_image_1 = PhotoImage(file="image_1.png")
image_1 = canvas.create_image(400.0, 250.0, image=image_image_1)

image_image_2 = PhotoImage(file="image_2.png")
image_2 = canvas.create_image(130.0, 200.0, image=image_image_2)

image_image_3 = PhotoImage(file="image_3.png")
image_3 = canvas.create_image(270.0, 200.0, image=image_image_3)

image_image_4 = PhotoImage(file="image_4.png")
image_4 = canvas.create_image(200.0, 101.0, image=image_image_4)

image_image_5 = PhotoImage(file="image_5.png")
image_5 = canvas.create_image(200.0, 309.0, image=image_image_5)

image_image_6 = PhotoImage(file="image_6.png")
image_6 = canvas.create_image(200.0, 411.0, image=image_image_6)

# Load and create buttons (keep references)
report_button_image = PhotoImage(file="report_button.png")
report_button = Button(
    image=report_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("report_button clicked"),
    relief="flat",activebackground='#0c4a96',bd=0
)
report_button.place(x=502.0, y=348.0, width=150.0, height=50.0)

help_button_image = PhotoImage(file="help_button.png")
help_button = Button(
    image=help_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("help_button clicked"),
    relief="flat",activebackground='#0c4a96',bd=0
)
help_button.place(x=502.0, y=246.0, width=150.0, height=50.0)

start_button_image = PhotoImage(file="start_button.png")
start_button = Button(
    image=start_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_loading_screen(),
    relief="flat", activebackground='#0c4a96',bd=0
)
start_button.place(x=477.0, y=125.0, width=200.0, height=50.0)


start_button_hover = PhotoImage(file='start_button_hover.png')
report_button_hover = PhotoImage(file='report_button_hover.png')
help_button_hover = PhotoImage(file='help_button_hover.png')

# Hover effects
def on_enter_start(event):
    start_button.config(image=start_button_hover)
def on_leave_start(event):
    start_button.config(image=start_button_image)
def on_enter_report(event):
    report_button.config(image=report_button_hover)
def on_leave_report(event):
    report_button.config(image=report_button_image)
def on_enter_help(event):
    help_button.config(image=help_button_hover)
def on_leave_help(event):
    help_button.config(image=help_button_image)



def show_loading_screen():
    # Hide the main window
    window.withdraw()

    # Create a separate window for the splash screen
    splash = tk.Toplevel(window)
    splash.geometry("288x480")
    splash.overrideredirect(True)

    # Center the splash screen on the screen
    splash_width = 288
    splash_height = 480
    splash_position_top = int(screen_height / 2 - splash_height / 2)
    splash_position_left = int(screen_width / 2 - splash_width / 2)
    splash.geometry(f'{splash_width}x{splash_height}+{splash_position_left}+{splash_position_top}')

    # Load GIF and setup animation
    gif_image = Image.open("loading.gif")
    gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_image)]

    # Display the frames in sequence
    gif_label = tk.Label(splash)
    gif_label.pack()

    def animate(frame_index=0):
        if gif_label.winfo_exists():  # Check if the label still exists
            gif_label.config(image=gif_frames[frame_index])
            frame_index = (frame_index + 1) % len(gif_frames)
            splash.after(100, animate, frame_index)  # Loop the animation with 100 ms delay

    # Start the animation
    animate()

    # Run the main task in the background
    threading.Thread(target=run_main_task, args=(splash,)).start()

def run_main_task(splash):
    time.sleep(2)  # Simulate loading timegt
    splash.destroy()  # Close splash screenrtf+666998/**tr5eds+88888888+;.llllllzA:"?///

    os.system("C:\\Users\\xstru\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\Users\\xstru\\Desktop\\Engr.Gutierrez\\Programming\\CODES\\Codesss\\Staad_shortcuts\\XSTRUCT_PRO_ENHANCE_v2\\PRO_ENHANCE_INTERFACE.py")


# Bind hover events
start_button.bind("<Enter>", on_enter_start)
start_button.bind("<Leave>", on_leave_start)
report_button.bind("<Enter>", on_enter_report)
report_button.bind("<Leave>", on_leave_report)
help_button.bind("<Enter>", on_enter_help)
help_button.bind("<Leave>", on_leave_help)



# Make window non-resizable
window.resizable(False, False)

# Keep references to images to prevent garbage collection
window.image_refs = [image_image_1, image_image_2, image_image_3, image_image_4, image_image_5, image_image_6,
                     report_button_image, help_button_image, start_button_image]

# Start the Tkinter main loop
window.mainloop()
