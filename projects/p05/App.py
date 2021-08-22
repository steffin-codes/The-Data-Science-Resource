import streamlit as st
import cv2
from PIL import Image
import numpy as np
#TODO: Face Detection
def app():
    #? Project Inputs
    # st.sidebar.subheader("Project Inputs:")
    st.title("P05: Face Detection using OpenCV")
    uploaded_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])

    face_cascade = cv2.CascadeClassifier('projects\p05\haarcascade_frontalface_default.xml')
    # Read the input image
    if uploaded_file is not None:
        scaleFactor = st.slider('scaleFactor?', 1.01, 2.0, 1.1)
        minNeighbors = st.slider('minNeighbors?', 1, 20, 10)
        detect = st.button(label="Detect Faces!")
        pil_image = Image.open(uploaded_file).convert('RGB') 
        open_cv_image = np.array(pil_image) 
        orig_image = open_cv_image
        col1,col2 = st.columns([1,1])
        with col1:
            st.subheader("Image")
            st.image(open_cv_image)
        with col2:
            if (detect):
                st.subheader("Face Detected")
                # Convert into grayscale
                gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
                # Detect faces
                # faces = face_cascade.detectMultiScale(gray, i, 5)
                faces = face_cascade.detectMultiScale(image=gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(20,20))
                # Draw rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(orig_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
                st.image(orig_image)