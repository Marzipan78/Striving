import aflr
import key
# Add your AFLR_API_KEY here - get it from https://console.api.audio/register aflr 
aflr.api_key = key.api_key
# There are 180+ voices to choose from. Try "Joanna", "Amy", or "Salli"
VOICE="es-ES-AlvaroNeural"
# Apply a voice effect. Can be dark_father, chewie, 88b, 2r2d
#EFFECT="dark_father"
TEXT = """Eh FUCK Of"""
SPEED=90
# May the 4th background tracks
# full__fargalaxy_dark_father.wav
# full__fargalaxy_chewie.wav
#full__fargalaxy_droid.wav
#BACKGROUNDTRACK="full__fargalaxy_dark_father.wav"

# script creation
script = aflr.Script().create(
    scriptText=TEXT,
    projectName="Jon",
    moduleName="evil",
    scriptName=f"Jon",
)
print(f"Connect to the dev star: \n {script} \n")

# get the scriptId from the script created.
scriptId = script["scriptId"]


# speech creation
response = aflr.Speech().create(
  
    scriptId=scriptId, voice=VOICE, speed=SPEED
)
print(f"Response from dev star: \n {response} \n")
# mastering process
response = aflr.Mastering().create(
    scriptId=scriptId, 
)
print(f"Using the force: \n {response} \n")

# get url of audio tracks generated
url = aflr.Mastering().retrieve(scriptId=scriptId)
#print(f"url to download the track: \n {url} \n")

# or download
file = aflr.Mastering().download(
    scriptId=scriptId,  destination="."
)
print(f"Listen to the results of the force: \n {file} \n")


