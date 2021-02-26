import cv2
import streamlit as st


st.title("Simple Webcam App using Streamlit")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)


run = True

if st.button('Stop'):
    run = False

while (run):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame, use_column_width=True)

camera.release()
cv2.destroyAllWindows()
