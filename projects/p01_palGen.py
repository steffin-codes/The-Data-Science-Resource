from operator import mod
import streamlit as st
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image # using this to open image...
# TODO: give a search functionality to the posts...
# this is amazing!!
# https://github.com/streamlit/demo-self-driving/blob/5f8e500dc8ccf914051859b905361d7a52d22dda/streamlit_app.py
def app():

    def rgb_to_hex(rgb_color):
        # function to convert rgb color to hex codes
        hex_color = "#"
        for i in rgb_color: hex_color += ("{:02x}".format(int(i)))
        return hex_color

    def prep_image(raw_img):
        # function to resize and reshape before feeding to classifier
        modified_img = cv2.resize(raw_img, raw_img.shape[:2], interpolation = cv2.INTER_AREA) #optional
        modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3) #required
        return modified_img
 
    # project inputs
    st.title("Palette generator using K-Means")
    st.write("Presenting a simple implementation of the K-means ML algorithm. This web app requires an image, which will be fed to the K-means algorithm, which will detect the colors and calculates the wieghts of each color. This is then graphed into a pie chart that looks like a Palette!")
    st.sidebar.subheader("Project Inputs:")
    uploaded_file = st.sidebar.file_uploader("Upload Image",type=['png','jpeg'],help="Bigger the image accurate the clustering would be!")
    n_clusters = st.sidebar.slider('Value of K?', 1, 10, 4,help="No of colors!")
    generate = st.sidebar.button("Generate",help="Clicke me to generate the chart!")
    
    if uploaded_file is not None:
        # orig_image = None
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        orig_image = opencv_image
        col1,col2 = st.beta_columns([1,1])
        with col1:
            st.subheader("Image")
            st.image(orig_image)
        with col2:
            if (generate):
                st.subheader("The Palette using k={}".format(n_clusters))
                modified_image = prep_image(orig_image)
                clf,color_labels,center_colors,counts,ordered_colors,hex_colors=None,None,None,None,None,None
                clf = KMeans(n_clusters=n_clusters)
                color_labels = clf.fit_predict(X=modified_image,y=None)
                center_colors = clf.cluster_centers_
                counts = Counter(color_labels)
                ordered_colors = [center_colors[i] for i in counts.keys()]
                hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
                fig, ax = plt.subplots()
                ax.pie(counts.values(), labels = hex_colors, colors = hex_colors)
                st.pyplot(fig)
    else:
        st.warning("👈🏼 Head over to the sidebar and upload an image!")    
    pass