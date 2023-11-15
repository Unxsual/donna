# Loading GPT 3.5, functional chatbot in terminal

## sudo apt install python3-pip
## pip install openai
## pip install gTTS

from typing import Mapping
import openai
from gtts import gTTS
import os

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

a = input()
messages=[{"role": "user", "content": a}]

response = openai.ChatCompletion.create(
model="gpt-3.5-turbo")

print(response)

# Generating audio file for audio response

tts = gTTS(text=response['choices'][0]['text'], lang='en')
tts.save("response.mp3")
os.system("mpg123 response.mp3")
yon = input()
if yon == 'yes':
  os.remove("response.mp3")

