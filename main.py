import glob
import customtkinter
import threading

from tkinter import messagebox, filedialog
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    WIDTH = 350
    HEIGHT = 200

    def __init__(self):
        super().__init__()

        self.title("HD2SD")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(False, False)
        self.iconbitmap("icon.ico")

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
        self.button_folder.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

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
            text="Convert HD to SD",
            command=self.start_convert,
        )
        self.button_convert.place(relx=0.5, rely=0.62, anchor=customtkinter.CENTER)
        self.button_convert.configure(state="disabled")

        self.progressbar = customtkinter.CTkProgressBar(master=self, width=250)
        self.progressbar.place(relx=0.5, rely=0.73, anchor=customtkinter.CENTER)
        self.progressbar.set(0)

    def start_convert(self):
        threading.Thread(target=self.convert).start()
        self.progressbar.set(0)

    def convert(self):
        n = 0
        confirm = messagebox.askquestion(
            "HD2SD", "Are you sure you want to convert your HD files to SD?"
        )
        if confirm == "yes":
            hd_images = glob.glob(rf"{filename}/*@2x.png")

            for i in hd_images:
                n += 0.1
                hd_image = Image.open(i)
                x, y = hd_image.size
                sd_image = hd_image.resize((x // 2, y // 2))
                name, suffix = i.split("@")
                sd_image.save(f"{name}.png")
                self.progressbar.set(round(n))
        else:
            pass

    def select_folder(self):
        global filename
        filename = filedialog.askdirectory()
        self.button_convert.configure(state="normal")
        self.entry.configure(
            state="normal", placeholder_text=filename.split("Skins/")[1]
        )
        self.entry.configure(state="disabled")
        self.button_folder.configure(text="Change Skin Folder")

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
