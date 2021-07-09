
import key
import aflr
import os
from pytube import YouTube

def aflr_create(scriptName, message):
    aflr.api_key = key.api_key
    script = aflr.Script().create(scriptText= message, scriptName=scriptName, moduleName="video", projectName="new_video")
    print(script)
    response = aflr.Speech().create(scriptId=script.get("scriptId"), voice="Matthew", speed = "80", effect ="dark_father",silence_padding = str(1000 * 2))
    print(response)
    if scriptName == "audio":
        response = aflr.Mastering().create(scriptId=script.get("scriptId"),backgroundTrackId="full__fargalaxy_dark_father.wav")
        print(response)
    elif scriptName == "speech":
        response = aflr.Mastering().create(scriptId=script.get("scriptId"))
        print(response)
    response = aflr.Mastering().download(scriptId=script.get("scriptId"), destination=".")
    print(response)
    
def downloadYouTube(videourl, filename):
    yt = YouTube(videourl)
    yt.streams.get_highest_resolution().download(filename = "./" + filename)

    
def combine_audio(video, speech, audio):
    os.system(f'ffmpeg -i {video} -i {speech} -filter_complex "[0:a]volume=0.4[a0]; [1:a]volume=0.9[a1]; [a0][a1]amix=duration=longest[a]" -map 0:v -map "[a]" -c:v copy overlayAudio.mp4')
    os.system(f'ffmpeg -i {video} -i {audio} -filter_complex "[0:a]volume=0.0[a0]; [1:a]volume=1.0[a1]; [a0][a1]amix=duration=longest[a]" -map 0:v -map "[a]" -c:v copy substituteAudio.mp4')
    
def download_create():
    text = "<break time='3s'/>You can't stop change any more than you can stop the suns from setting. <break time='1s'/> Join the dark force"    
    downloadYouTube("https://youtu.be/tpJ2EVR4L3w", "downloadedVideo")
    tracks = ["speech", "audio"]
    for track in tracks:
        aflr_create(track, text)
    combine_audio("downloadedVideo.mp4", "speech.mp3", "audio.mp3")
download_create()




