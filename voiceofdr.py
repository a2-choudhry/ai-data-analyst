#google text to speech (gtts and elevenlabs)
import os
from gtts import gTTS

# def text_to_speech_gtts(input_text, output_filepath):
#     language='en'

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)

# input_text="Hi this is rafay ai testing"
# text_to_speech_gtts(input_text, output_filepath="gtts_testing.mp3")

import elevenlabs
from elevenlabs.client import ElevenLabs

from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

# fetch key
api_key = os.getenv("ELEVEN_API_KEY")


# def text_to_speech_elevenlabs(input_text,output_filepath):
#     client = ElevenLabs(api_key=api_key)
#     audio=client.text_to_speech.convert(
#         text=input_text,
#         voice_id='zZLmKvCp1i04X8E0FJ8B',
#         output_format="mp3_22050_32",
#         model_id='eleven_turbo_v2'
#     )

#     elevenlabs.save(audio,output_filepath)
# text_to_speech_elevenlabs(input_text, output_filepath="eleven_labs_testing.mp3")




# #eleven labs- use ai voice generator.
import subprocess
import platform
from pydub import AudioSegment
import io

def text_to_speech_gtts(input_text, output_filepath):
    language='en'

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name= platform.system()
    

def text_to_speech_elevenlabs(input_text,output_filepath):
    client = ElevenLabs(api_key=api_key)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id='zZLmKvCp1i04X8E0FJ8B',
        output_format="mp3_22050_32",
        model_id='eleven_turbo_v2'
    )

    elevenlabs.save(audio, output_filepath)
    
    audio = AudioSegment.from_mp3(output_filepath)
    audio.export(output_filepath, format="wav")

    os_name= platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
#text_to_speech_elevenlabs(input_text, output_filepath="eleven_labs_autoplay_testing.mp3")
