import requests
import streamlit as st
import io
from PIL import Image
from datetime import datetime

headers = {"Authorization": "Bearer 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"}

def text2image(prompt):
  API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
  payload = {
      "inputs": prompt,
  }
  response = requests.post(API_URL, headers=headers, json=payload)
  return Image.open(io.BytesIO(response.content))


def text2speech(prompt):
  API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
  payload = {
      "inputs": prompt,
  }
  response = requests.post(API_URL, headers=headers, json=payload)

  return response.content

def main():
  st.set_page_config(page_title="AI Image and Speech Generator", page_icon="/content/drive/MyDrive/Colab Notebooks/AI Application/PageIcon.png")
  st.header("AI Image and Speech Generator")
  prompt = st.text_input("Your prompt")

  if prompt is not None:
    #generating image
    image = text2image(prompt)

    with st.expander("Image Generated"):
      st.image(image=image)

    #generating audio
    speech = text2speech(prompt)

    with st.expander("Audio Generated"):
      st.audio(speech)


if __name__ == '__main__':
  main()