import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from PIL import Image, ImageTk, ImageSequence
import threading
import time
from PRO_ENHANCE_INTERFACE import Interface
import urllib.parse
import webbrowser
import sys
import os

class MainWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        # Create the main window
        self.title("XSTRUCT PRO ENHANCE v2")
        self.geometry("800x500")
        self.configure(bg="#006AEC")

        # Center the main window on the screen
        window_width = 800
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

        # Load the icon image in a valid format (e.g., PNG)
        icon_image = Image.open(self.get_resource_path("Icon.ico"))
        self.iconphoto(False, ImageTk.PhotoImage(icon_image))

        # Create a canvas
        canvas = Canvas(self, bg="#006AEC", height=500, width=800, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # Load and create image elements (keep references)
        image_image_1 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_1.png"))
        canvas.create_image(400.0, 250.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_2.png"))
        canvas.create_image(130.0, 200.0, image=image_image_2)

        image_image_3 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_3.png"))
        canvas.create_image(270.0, 200.0, image=image_image_3)

        image_image_4 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_4.png"))
        canvas.create_image(200.0, 101.0, image=image_image_4)

        image_image_5 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_5.png"))
        canvas.create_image(200.0, 309.0, image=image_image_5)

        image_image_6 = PhotoImage(file=self.get_resource_path("images_mainmenu/image_6.png"))
        canvas.create_image(200.0, 411.0, image=image_image_6)

        # Load and create buttons (keep references)
        report_button_image = PhotoImage(file=self.get_resource_path("images_mainmenu/report_button.png"))
        report_button = Button(
            self, image=report_button_image, borderwidth=0, highlightthickness=0,
            command=self.open_email_client, relief="flat", activebackground='#0c4a96', bd=0
        )
        report_button.place(x=502.0, y=348.0, width=150.0, height=50.0)

        help_button_image = PhotoImage(file=self.get_resource_path("images_mainmenu/help_button.png"))
        help_button = Button(
            self, image=help_button_image, borderwidth=0, highlightthickness=0,
            command=lambda: webbrowser.open("https://www.facebook.com/@xstructures"),
            relief="flat", activebackground='#0c4a96', bd=0
        )
        help_button.place(x=502.0, y=246.0, width=150.0, height=50.0)

        start_button_image = PhotoImage(file=self.get_resource_path("images_mainmenu/start_button.png"))
        start_button = Button(
            self, image=start_button_image, borderwidth=0, highlightthickness=0,
            command=self.show_loading_screen, relief="flat", activebackground='#0c4a96', bd=0
        )
        start_button.place(x=477.0, y=125.0, width=200.0, height=50.0)

        start_button_hover = PhotoImage(file=self.get_resource_path('images_mainmenu/start_button_hover.png'))
        report_button_hover = PhotoImage(file=self.get_resource_path('images_mainmenu/report_button_hover.png'))
        help_button_hover = PhotoImage(file=self.get_resource_path('images_mainmenu/help_button_hover.png'))

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

        # Bind hover events
        start_button.bind("<Enter>", on_enter_start)
        start_button.bind("<Leave>", on_leave_start)
        report_button.bind("<Enter>", on_enter_report)
        report_button.bind("<Leave>", on_leave_report)
        help_button.bind("<Enter>", on_enter_help)
        help_button.bind("<Leave>", on_leave_help)

        # Make window non-resizable
        self.resizable(False, False)

        # Keep references to images to prevent garbage collection
        self.image_refs = [
            image_image_1, image_image_2, image_image_3, image_image_4, image_image_5, image_image_6,
            report_button_image, help_button_image, start_button_image,
            start_button_hover, report_button_hover, help_button_hover
        ]

    def open_email_client(self):
        user_email = "xstructures.lowrence@gmail.com"
        subject = "Bug Report"

        if hasattr(self, 'description_text'):
            body = self.description_text.get("1.0", tk.END).strip()
        else:
            body = "Please describe the issue here."

        subject_encoded = urllib.parse.quote(subject)
        body_encoded = urllib.parse.quote(body)

        gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={user_email}&su={subject_encoded}&body={body_encoded}"

        webbrowser.open(gmail_link)
    def show_loading_screen(self):
        # Hide the main window
        self.withdraw()

        # Create a separate window for the splash screen
        splash = tk.Toplevel(self)
        splash.geometry("288x480")
        splash.overrideredirect(True)

        # Center the splash screen on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        splash_width = 288
        splash_height = 480
        splash_position_top = int(screen_height / 2 - splash_height / 2)
        splash_position_left = int(screen_width / 2 - splash_width / 2)
        splash.geometry(f'{splash_width}x{splash_height}+{splash_position_left}+{splash_position_top}')

        # Load GIF and setup animation
        gif_path = self.get_resource_path("images_sidebar/loading.gif")

        gif_image = Image.open(gif_path)
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
        threading.Thread(target=self.run_main_task, args=(splash,), daemon=True).start()

    def run_main_task(self, splash):
        time.sleep(2)  # Simulate loading time

        # Schedule the splash screen destruction and interface creation in the main thread
        self.after(0, splash.destroy)
        self.after(0, self.create_interface)

    def create_interface(self):
        """Create the Interface window."""
        app = Interface(master=self)  # Pass the current window as master
        app.mainloop()

    def get_resource_path(self, relative_path):
        """
        Returns the absolute path to a resource, handling both frozen and non-frozen environments.
        """
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS  # If running as a bundled app (PyInstaller)
        else:
            base_path = os.path.abspath(".")  # If running as a normal Python script
        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.withdraw()  # Use tk.Tk() instead of the MainWindow
    main_window = MainWindow(master=root)
    main_window.mainloop()