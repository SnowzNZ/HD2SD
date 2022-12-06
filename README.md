# HD2SD

<img src="https://media.discordapp.net/attachments/1044134327434358847/1049529615762333716/image.png">

High Definition to Standard Definition converter for osu! skins.

Contact: <https://twitter.com/Snowz2k>

I am not responsible for any damage caused to your skins by this program. This can be caused by overwriting files. Make sure to backup any important files before running.

## Usage

- Download [latest release](https://github.com/SnowzNZ/HD2SD/releases/latest)

    - Run HD2SD.exe

- Building from source

    - Download ZIP and extract it or `git clone https://github.com/SnowzNZ/HD2SD`
    - `cd HD2SD`
    - `pip install -r requirements.txt`
    - `pyinstaller --noconfirm --onefile --windowed --add-data "%localappdata%/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/"  "main.py"`
