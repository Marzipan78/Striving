# pip install -U pytube aflr 

import aflr
import os

def aflr_create(scriptName, message):
    aflr.api_key = 
    script = aflr.Script().create(scriptText= message, scriptName=scriptName, moduleName="video", projectName="new_video")
    print(script)
    response = aflr.Speech().create(scriptId=script.get("scriptId"), voice="Joanna", speed = "100", silence_padding = str(1000 * 2))
    print(response)
    if scriptName == "audio":
        response = aflr.Mastering().create(scriptId=script.get("scriptId"),backgroundTrackId="full__deepsea.wav")
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
    text = "<break time='5s'/>This could be your video voice over <break time='1s'/> Write your text here! Add breaks and personalisation parameters. Choose from our list of 180+ speakers. There are voices in Spanish, Enlgish, German and more! Create beautiful video voice overs."    
    downloadYouTube("https://www.youtube.com/watch?v=exXgMvbiCcU", "downloadedVideo")
    tracks = ["speech", "audio"]
    for track in tracks:
        aflr_create(track, text)
    combine_audio("downloadedVideo.mp4", "speech.mp3", "audio.mp3")
download_create()




