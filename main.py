import os
os.system("pip install --upgrade pip")
os.system("pip install openai")
os.system("pip install speechrecognition")
os.system("pip install openai==0.28")
import openai
from typing import Mapping
from gtts import gTTS
import speech_recognition as sr

openai.api_key = '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'

recognizer = sr.Recognizer()
# Ask for speech input
print("Hello, I am DONNA, your personal secretary. What's up?")
mth = input()
if mth == 1:
  with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)
    input_text = recognizer.recognize_google(audio)
if mth == 2:
  input_text = input("What's on your mind?")
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

while True:
  print('Anything else?')
  input_text = input('Enter your response:')
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo")

  print(response)
  tts = gTTS(text=response['choices'][0]['text'], lang='en')
  tts.save("response.mp3")
  os.system("mpg123 response.mp3")