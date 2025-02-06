!pip install ollama 
import os
import requests
import ollama 
from ollama import chat
from ollama import ChatResponse

import subprocess

#Start Ollama Engine
subprocess.Popen(["ollama", "serve"])

#Pull Model

!ollama pull llama3.2-vision



# Function to send a prompt to the model
def send_ollama_request(image_path):
   
    message_list=[
      {
      "role": "system",
      "content": "Only output valid JSON. Do not include any extra text, explanations, or markdown formatting."
      },
      {
      "role": "user",
      "content": "Extract data from this document and put it into Json",
      "images": [image_path]
      }
    ]
   
    response: ChatResponse = chat(model='llama3.2-vision',messages=message_list)
    #access fields directly from the response object
    print(response.message.content)    

    

send_ollama_request("Samples/employment1.png") 

    



