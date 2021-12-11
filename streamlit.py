import cv2
import streamlit as st

st.title("Emotion classifier")
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(-1)

ret, img = cam.read()
while ret:
# while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)


# import streamlit as st
# import cv2
# def draw_boxes(frame, boxes, threshold):
#     #drawing implementation
#     return frame
# def detect_objects(img):
#     #detection implementation
#     return [((0, 0, 1, 1), 1, 0.5),] #list of detections
# cam = cv2.VideoCapture(0)
# st_frame = st.empty()
# ret, img = cam.read()
# while ret:
#     ret, img = cam.read()
#     if ret:
#         detections = detect_objects(img)
#         img = draw_boxes(img, detections, 0.5)
#         st_frame.image(img, channels='BGR')