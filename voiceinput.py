#setup audio recorder (ffmpeg and portaudio)
# ffmpeg, portaudio, pyaudio
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_filepath="patient_voice_test_for_patient.mp3"
#record_audio(file_path=audio_filepath)


import os
#Speech to text STT model for transcript
from groq import Groq
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

# fetch key
api_key = os.getenv("GROQ_API_KEY")
stt_model="whisper-large-v3-turbo"
#audio_filepath="patient_voice_test_for_patient.mp3"

def groq_transcribe(stt_model,audio_filepath, api_key):

    client = Groq(api_key=api_key)
    
    #audio_file=open(audio_filepath,'rb')

    with open(audio_filepath, 'rb') as audio_file:
        transcription=client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
    )

    return transcription.text



