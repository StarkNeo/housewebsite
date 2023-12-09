from pathlib import Path
from openai import OpenAI
import openai

client = OpenAI()
#ENDPOINT TEXT TO AUDIO
from openai import OpenAI
client = OpenAI()

def textToAudio(text):
    speech_file_path = Path(__file__).parent/"static/answer.mp3"
    response = openai.audio.speech.create(
    model =  "tts-1",
    voice =  "alloy",   
    input = text
    )
    return response.stream_to_file(speech_file_path)

#ENDPOINT COMPLETITION


def consultant(topic):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system",
         "content":"You are Doctor Gregory House from the medical drama serie and you like to give briefly and sarcastic opinions about posible causes of health symptoms and address the consultants to visit a real doctor."},
        {"role":"user","content":f"{topic}"}
    ],
    #temperature=1.0,
   # max_tokens=100
    )
    return completion.choices[0].message.content



#ENDPOINT CREATE IMAGES

def imageGenerator():
    response =  client.images.generate(
        model =  "dall-e-3",
        prompt= """create a cook recipe instructions list in english language with an image: Bring the rice to a boil in a large pot of water and simmer for 30 minutes or until tender.

            """,
        size = "1024x1024",
        quality= "standard",
        n=1)
    return response.data[0].url
