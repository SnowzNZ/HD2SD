"""
Create SD images for osu! skins by downscaling HD images by 50%
"""

import glob
import os
import textwrap
from tkinter import filedialog

import readchar
from pick import pick
from PIL import Image
from tqdm import tqdm

print(
    """
HD2SD  Copyright (C) 2023  SnowzNZ
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
)

# Default location for osu! skins
default_skin_path = os.path.join(os.environ["LOCALAPPDATA"], "osu!", "Skins")

# Check if the path exists
if os.path.exists(default_skin_path):
    folder_path = filedialog.askdirectory(initialdir=default_skin_path)
else:
    folder_path = filedialog.askdirectory()

option, _ = pick(
    ["Yes", "No"],
    textwrap.fill(f"Selected Folder: {folder_path}")
    + "\n\nAre you sure you wish to continue?",
)

if option == "Yes":
    # Get every image in the folder
    for image in tqdm(
        glob.glob(rf"{folder_path}/*@2x.png"),
        desc="Downscaling images",
        unit=" images",
    ):
        # Open the HD image
        hd_image = Image.open(image)

        # Get the width and height of the image
        width, height = hd_image.size

        if width >= 2 and height >= 2:
            size = (width // 2, height // 2)
        else:
            size = (width, height)

        # Resize the image
        hd_image = hd_image.resize(size, Image.Resampling.LANCZOS)
        hd_image.save(image.replace("@2x", ""))

if option == "No":
    print("Press any key to exit...")
    key = readchar.readkey()
