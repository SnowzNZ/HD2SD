"""
Create SD images for osu! skins by downscaling HD images by 50%
"""

import glob
import os
import textwrap
import time
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

# Ask the user if they wish to continue
option, _ = pick(
    ["Yes", "No"],
    textwrap.fill(f"Selected Folder: {folder_path}")
    + "\n\nAre you sure you wish to continue?",
)

if option == "Yes":
    # Get start time of process
    start_time = time.time()

    # Get every image in the folder
    for image in tqdm(
        glob.glob(rf"{folder_path}/*@2x.png"),
        desc="Converting images to SD",
        unit=" image",
    ):
        # Open the HD image
        hd_image = Image.open(image)

        # Get the width and height of the image
        width, height = hd_image.size

        # Check if the image is more than 1x1, if not break out of the for loop as 1/2 != a whole number
        if width > 1 and height > 1:
            size = (width // 2, height // 2)
        else:
            break

        # Resize the image
        hd_image = hd_image.resize(size, Image.Resampling.LANCZOS)
        # Save the image as an SD image
        hd_image.save(image.replace("@2x", ""))

    # Get end time of process
    end_time = time.time()

    # Calculate total time it took
    elapsed_time = end_time - start_time

    # Print total time it took to complete
    print(f"\nCompleted in {round(elapsed_time, 3)} seconds.")

print("Press any key to exit...")
key = readchar.readkey()
