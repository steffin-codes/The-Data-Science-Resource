from Helper import GIT_REPO, IS_LOCAL
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
# from keras.models import load_model -> this got attribute error?
from tensorflow.keras.models import load_model


#TODO: A simple Handwritten Digit Recognition using CNN on the MINST dataset that accepts data from canvas

def app():
    if IS_LOCAL:
        model = load_model('projects/p03/mnist.h5',compile=False)
    else:
        model = load_model(GIT_REPO+'projects/p03/mnist.h5',compile=False)
    def predict_digit(img):
        print(img)
        #resize image to 28x28 pixels
        img = img.resize((28,28))
        #convert rgb to grayscale
        img = img.convert('L')
        img = np.array(img)
        #reshaping to support our model input and normalizing
        img = img.reshape(1,28,28,1)
        img = img/255.0
        #predicting the class
        res = model.predict([img])[0]
        print(res)
        return np.argmax(res), max(res)
    #? Project Inputs
    st.title("P03: Handwritten Digit Recognition")
    st.sidebar.subheader("Project Inputs:")
    # Specify canvas parameters in application
    stroke_width = 10
    stroke_color = "#000000"
    bg_color = "#FFFFFF"
    bg_image = None #st.sidebar.file_uploader("Image with number:", type=["png", "jpg","jpeg"])
    drawing_mode ="freedraw"
    # realtime_update = st.sidebar.checkbox("Update in realtime", True)
    col1,col2 = st.beta_columns([1,1])
    with col1:
        st.subheader("Drawable Canvas")
        # st.image()
        # Create a canvas component
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            background_image=Image.open(bg_image) if bg_image else None,
            update_streamlit=True,
            height=500,
            drawing_mode=drawing_mode,
            key="canvas",
            display_toolbar=True
        )
    generate = st.sidebar.button("Generate") 
    with col2:
        if generate:
            img = Image.fromarray(canvas_result.image_data, 'RGB')
            with img:
                predicted_digit,accuracy = predict_digit(img)
            st.subheader("Predicted to be {} with {} accuracy!".format(
                predicted_digit,
                str(round(accuracy*100, 2))))
            st.image(canvas_result.image_data)
            # st.write(
            #     type(canvas_result.image_data),
            #     # canvas_result.image_data,
            #     Image.fromarray(canvas_result.image_data, 'RGB')
            # )
            pass

        else:
            st.warning("👈🏼 Head over to the sidebar and upload an image!")    
        pass
    pass