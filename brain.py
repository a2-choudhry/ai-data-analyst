# #first set up GROQ API key
# import os
# #GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


import os
from groq import Groq
from dotenv import load_dotenv

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
# load .env file
load_dotenv()

# fetch key
api_key = os.getenv("GROQ_API_KEY")

#Step2: Convert image to required format
import base64

#image_path="exampleimage.jpg"
def img_encode(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


query="summerise this image into very concise manner?"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def analyse_image_query(query,model, encoded_image):
    client = Groq(api_key=api_key)
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content