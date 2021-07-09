#Check that you are using python 3.8 or further 
#pip install -U aflr
import aflr 
import key 
aflr.api_key= key.api_key

# Let's create a script!
text = "<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome."
script = aflr.Script().create(scriptText=text, scriptName="multiple_speakers")
print(script) 

# Create text to speech 
r = aflr.Speech().create(
    scriptId=script["scriptId"],
    voice="en-US-Standard-D",
    speed=90,
    silence_padding=0,
     sections={
        "question": {
            "voice": "Amy",
            "speed": 110,
            "silence_padding": 1000
        },
        "answer": {
            "voice": "en-GB-RyanNeural",
            "speed": 100,
        }
   
     }
)
print(r)

# Mastering creation 
r = aflr.Mastering().create(scriptId=script["scriptId"], backgroundTrackId="full__deepsea.wav")
print(r)

# retrieve the mastered audio files
r = aflr.Mastering().retrieve(scriptId=script["scriptId"])
print(r)

# download all speech audio files
# check your folder :) you should have the following audio_files
file = aflr.Mastering().download(scriptId=script.get("scriptId"), destination=".")
print(file)