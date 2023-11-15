# Loading GPT 3.5, functional chatbot in terminal

## sudo apt install python3-pip
## pip install openai
## pip install gTTS

import os
from typing import Mapping

import openai
import speech_recognition as sr
from gtts import gTTS

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY
# Initialize the recognizer
recognizer = sr.Recognizer()
# Ask for speech input
print(What's up?)
if method = 1:
  with sr.Microphone() as source:
    print("Speak something:")
    audio = recognizer.listen(source)
    input_text = recognizer.recognize_google(audio)
if method = 2:
  input_text = input()
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