from Helper import GIT_REPO, IS_LOCAL
import streamlit as st
import numpy as np
import cv2
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model

#TODO: A simple Handwritten Digit Recognition using CNN on the MINST dataset that accepts data from canvas

def app():

    MINST_MODEL = load_model('projects/p03/minst_model')
    #? Project Inputs
    st.title("P03: Handwritten Digit Recognition")
    col1,col2,col3 = st.beta_columns([1,1,1])
    with col1:
        stroke_width = 10
        stroke_color = "#FFFFFF"
        bg_color = "#000000"
        SIZE = 28*10
        st.subheader("Drawable Canvas - "+str(SIZE)+"x"+str(SIZE))
        # Create a canvas component
        canvas_result = st_canvas(
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            width=SIZE,
            height=SIZE,
            drawing_mode="freedraw",
            key='canvas')
        predict = st.button("Predict") 
    with col2:
        img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
        rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
        st.subheader("Rescaled Image 28X28")
        st.image(rescaled)
    with col3:
        if predict:
            test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            score = MINST_MODEL.predict(test_x.reshape(1, 28, 28))
            st.subheader(f'The number is predicted to be: {np.argmax(score[0])}')
            st.bar_chart(score[0])
            pass

        else:
            st.warning("👈🏼 Draw a number. Wait for it to load and click Predict!")    
        pass
    pass