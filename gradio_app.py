
import gradio as gr
from brain import img_encode, analyse_image_query
from voiceinput import record_audio, groq_transcribe
from voiceofdr import text_to_speech_elevenlabs, text_to_speech_gtts
import os
from dotenv import load_dotenv
load_dotenv()


system_prompt="""You are a professional Data Analyst. Do not mention that you are an AI. Always respond as a human analyst would in a business or technical setting.
Your responsibilities:
Analyze data: Use SQL/Python-like approaches.
Avoid filler or AI disclaimers
Mimic a human workflow: Write as if you are documenting your own analysis steps or presenting them in a meeting. Use terms like “I checked”, “the data shows”, or “let’s test this assumption”.
Be practical: Recommend next steps, sanity checks, and possible pitfalls.

Style guide:
Prioritize clarity and actionability.
Use bullet points, short paragraphs, and tables where appropriate.
If needed, show concise code snippets (Python/SQL) but focus on explaining the logic.
Never say “as an AI” or “I cannot”. Stay in character as a data analyst working alongside a team. your answer should mimic that of an actual data analyst not an AI bot, 
Keep your answer very concise and to the point. No preamble, start your answer right away please"""


def process_inputs(audio_file, img_filepath):
    speech_to_text_output = groq_transcribe(api_key = os.getenv("GROQ_API_KEY"), 
                                                 audio_filepath=audio_file,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if img_filepath:
        AI_response = analyse_image_query(query=system_prompt+speech_to_text_output, encoded_image=img_encode(img_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
    else:
        AI_response = "No image provided for me to analyze"

    AI_voice_response = text_to_speech_elevenlabs(input_text=AI_response, output_filepath="final.mp3") 

    txt_path = "ai_response.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(AI_response)

    return speech_to_text_output, AI_response, AI_voice_response, txt_path


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text", lines=4, max_lines=6),
        gr.Textbox(label="AI Response", lines=12, max_lines=20, scale=2),
        gr.Audio("Temp.mp3"),
        gr.File(label="Download Output") 
    ],
    title="AI data analyst"
)

iface.launch(debug=True)