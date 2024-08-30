import requests
import streamlit as st

url = "https://app.ayrshare.com/api/post"
headers = {
    "Authorization": "Bearer R62BEX1-PY8M6DS-P25EPTZ-76VSR8G",
    "Content-Type": "application/json"
  }
data = {
    "post": st.text_input("Insert the post's description here"),
    "platforms": ["linkedin"],
    "mediaUrls": st.file_uploader("Choose an image for the post", type=["jpg", "jpeg", "png"])
  }

response = requests.post(url, json=data, headers=headers)
st.write(response.json())
