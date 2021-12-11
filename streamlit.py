import cv2
import streamlit as st

st.title("Emotion classifier")
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(-1)

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)