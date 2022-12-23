"""
Program to convert HD images to SD
"""

import glob
import threading
from tkinter import filedialog, messagebox

import customtkinter  # type: ignore
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    """GUI"""

    WIDTH = 350
    HEIGHT = 200

    def __init__(self):
        super().__init__()

        self.title("HD2SD")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(False, False)
        self.filename = None

        self.button_folder = customtkinter.CTkButton(
            master=self,
            width=250,
            height=30,
            border_width=0,
            corner_radius=30,
            text="Select Skin Folder",
            command=self.select_folder,
            text_color_disabled="#000",
        )
        self.button_folder.place(
            relx=0.5, rely=0.2, anchor=customtkinter.CENTER
        )

        self.entry = customtkinter.CTkEntry(
            master=self, placeholder_text="", state="disabled", width=250
        )
        self.entry.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        self.button_convert = customtkinter.CTkButton(
            master=self,
            width=250,
            height=30,
            border_width=0,
            corner_radius=30,
            text="Convert!",
            command=self.start_convert,
        )
        self.button_convert.place(
            relx=0.5, rely=0.62, anchor=customtkinter.CENTER
        )
        self.button_convert.configure(state="disabled")

        self.progressbar = customtkinter.CTkProgressBar(master=self, width=250)
        self.progressbar.place(
            relx=0.5, rely=0.73, anchor=customtkinter.CENTER
        )
        self.progressbar.set(0)

    def start_convert(self):
        """Start the convert function"""
        threading.Thread(target=self.convert).start()
        self.progressbar.set(0)

    def convert(self):
        """Convert all @2x images to SD"""
        images_converted = 0
        confirm = messagebox.askquestion(
            "HD2SD", "Are you sure you want to convert your HD files to SD?"
        )
        if confirm == "yes":
            hd_images = glob.glob(rf"{self.filename}/*@2x.png")

            for i in hd_images:
                images_converted += 1
                progress = images_converted / len(hd_images)
                hd_image = Image.open(i)
                x_pos, y_pos = hd_image.size
                if x_pos >= 2 and y_pos >= 2:
                    size = (x_pos // 2, y_pos // 2)
                else:
                    size = (x_pos, y_pos)
                hd_image = hd_image.resize(size, Image.Resampling.LANCZOS)
                name = i.split("@")
                hd_image.save(f"{name}.png")
                self.progressbar.set(progress)
            messagebox.showinfo("HD2SD", "Conversion Complete!")
        else:
            pass

    def select_folder(self):
        """Choose folder to convert"""
        self.filename = filedialog.askdirectory()
        self.button_convert.configure(state="normal")
        self.entry.configure(
            state="normal", placeholder_text=self.filename.split("Skins/")[1]
        )
        self.entry.configure(state="disabled")
        self.button_folder.configure(text="Change Skin Folder")
        self.progressbar.set(0)

    def on_closing(self):
        """Destroy window on close"""
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
