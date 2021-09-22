from youtube_transcript_api import YouTubeTranscriptApi
import json
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
import pandas as pd
from time import strftime
from time import gmtime

def video_transcript(data):
    video_id = data
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id)
    #time_stamps = WebVTTFormatter().format_transcript(transcript)
    df = pd.DataFrame(transcript)
    timestamp = []
    for i in range(0,len(df)):
        timestamp.append(strftime("%H:%M:%S", gmtime(df['start'].iloc[i])))
    df['timestamp'] = timestamp
    df.to_csv('transcript.csv', index=False)
    return df
