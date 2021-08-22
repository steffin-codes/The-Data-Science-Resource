import streamlit as st
from PIL import Image
import cv2
import numpy as np
# TODO: Cartoonifying Image using K-means Classifier Algorithm
def app():
    def edge_mask(img, line_size, blur_value):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, blur_value)
        edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
        return edges
    def color_quantization(img, k):
        # Transform the image
        data = np.float32(img).reshape((-1, 3))
        # Determine criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
        # Implementing K-Means
        ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        result = center[label.flatten()]
        result = result.reshape(img.shape)
        return result
    #! Project Inputs
    st.title("P02: Cartoonify Image using K-Means")
    st.sidebar.subheader("Project Inputs:")
    uploaded_file = st.sidebar.file_uploader("Upload Image",type=['png','jpeg','jpg'],help="Bigger the image accurate the clustering would be!")
    line_size = st.sidebar.slider('Line Size:', 4, 10, 9,help="Thickness of the line")
    blur_value = st.sidebar.slider('Blur:', max(2,line_size), line_size, min(3,line_size),help="Thickness of the line")
    total_color = st.sidebar.slider('Total Colors:', 1, 20, 9,help="Number of clusters")
    generate = st.sidebar.button("Generate") 
    if uploaded_file is not None:
        '''
        So cv.imread of fileuploader image is not feasible
        So used a hacky PIL library just to open the image
        '''
        pil_image = Image.open(uploaded_file).convert('RGB') 
        open_cv_image = np.array(pil_image) 
        orig_image = open_cv_image
        col1,col2 = st.columns([1,1])
        with col1:
            st.subheader("Image")
            st.image(orig_image)
        with col2:
            if (generate):
                st.subheader("Cartoonified Image")
                edges = edge_mask(orig_image, line_size, blur_value)
                img = color_quantization(orig_image, total_color)
                blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
                cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
                st.image(cartoon)
            else:
                st.warning("👈🏼 Head over to the sidebar and click Generate!")    
    else:
        st.warning("👈🏼 Head over to the sidebar and upload an image!")    
    pass