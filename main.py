import os
from moviepy.editor import *
import requests
import urllib.request
import glob
import secrets
from random import randint

def logStr(string):
    print("")
    print("=================================")
    print(string)
    print("=================================")
    print("")
    
def getVideo(link):
    logStr("Finding media links")
    r = requests.get(redditLink + ".json", headers = {'User-agent': str(randint(0,10000)})
    videoLink = r.json()[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
    logStr("Getting video and audio data")
    urllib.request.urlretrieve(
        videoLink,
        filename="tmp/video.mp4",
    )
    audioLink = videoLink.split("DASH_")[0] + "DASH_audio.mp4" + videoLink.split(".mp4")[1]
    urllib.request.urlretrieve(
        audioLink,
        filename="tmp/audio.mp4",
    )
    logStr("Combining video and audio")
    clip = VideoFileClip("tmp/video.mp4")

    h = AudioFileClip("tmp/audio.mp4")
    h.write_audiofile("tmp/video.mp3")
    audioclip = AudioFileClip("tmp/video.mp3")

    videoclip = clip.set_audio(audioclip)

    videoclip.write_videofile("output/output.mp4")
    
def clearTempFiles():
    logStr("Clearing temporary files")
    files = glob.glob("tmp/*")
    for f in files:
        os.remove(f)

redditLink = input("Post link: ")
getVideo(redditLink)
clearTempFiles()