import youtube_dl
import ffmpeg
import os
from utils.randomize import randomize as passwordz

async def playlistgen(url):
    print("---[Request]---")
    print(f"URL = {url}")
    passgen = await passwordz()
    print(f"FileName = {passgen}.txt")
    os.popen(f"youtube-dl --get-id --ignore-errors {url} > 'music/{passgen}.txt'").read()
    return f"{passgen}.txt"