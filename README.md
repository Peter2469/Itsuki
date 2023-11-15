# Itsuki
### A Discord Bot created in Python.

## Installation Guide

1. Install wget (Linux only)
2. Install python3
3. Install python3-pip
4. Install git
5. Install all pip3 packages
    ```bash
    pip3 install -U discord.py[voice] && pip3 install -U dblpy && pip3 install -U hurry.filesize && pip3 install -U praw && pip3 install -U gtts && pip3 install -U mutagen && pip3 install -U urbandictionary && pip3 install -U SpeechRecognition && pip3 install -U tinytag && pip3 install -U psutil && pip3 install -U nbapi && pip3 install -U pyowm && pip3 install -U PyDictionary && pip3 install -U random_word && pip3 install -U pillow && pip3 install -U youtube-dl && pip3 install -U ffmpeg && pip3 install -U pynacl
    ```
6. Clone Repo
    ```bash
    git clone https://github.com/Peter2469/Itsuki
    ```
7. (Optional/Linux only) Install pm2
    ```bash
    wget -qO- https://getpm2.com/install.sh | bash
    ```
8. Open `secret.py` from the cloned repo and enter the necessary details.
9. Run the bot.
    ```bash
    PM2 (Linux):
    pm2 start main.py --interpreter "/usr/bin/python3" --interpreter-args -- cogs music
    ```

## Disclaimer
This Discord bot was last updated in 2020, and development has been discontinued. As a result, the code may no longer work with the latest dependencies and Discord API changes. It is recommended not to use this bot directly without updating the code. If you encounter issues during installation, consider checking for community updates or seeking assistance in relevant forums.

Please note that dependencies and libraries may have been updated since the last release, and it's advisable to periodically check for updates and adjust the installation instructions accordingly.
