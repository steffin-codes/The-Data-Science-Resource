import streamlit as st
from PIL import Image
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt
#TODO: Palette Generator using K-means Classifier Algorithm
def app():
    def rgb_to_hex(rgb_color):
        '''
        function to convert 
        (0,0,0) -> #000000
        (255,255,255) -> #ffffff
        '''
        hex_color = "#"
        for i in rgb_color: hex_color += ("{:02x}".format(int(i)))
        return hex_color
    def prep_image(raw_img):
        '''
        function to clean image
        '''
        modified_img = cv2.resize(raw_img, raw_img.shape[:2], interpolation = cv2.INTER_AREA) #optional
        modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3) #required
        return modified_img
    #? Project Inputs
    st.sidebar.subheader("Project Inputs:")
    st.title("P01: Palette Generator using K-Means")
    uploaded_file = st.sidebar.file_uploader("Upload Image",type=['png','jpeg'],help="Bigger the image accurate the clustering would be!")
    n_clusters = st.sidebar.slider('Value of K?', 1, 10, 4,help="Number of colors!")
    generate = st.sidebar.button("Generate") 
    if uploaded_file is not None:
        '''
        So cv.imread of fileuploader image is not feasible
        So used a hacky PIL library just to open the image
        '''
        pil_image = Image.open(uploaded_file).convert('RGB') 
        open_cv_image = np.array(pil_image) 
        orig_image = open_cv_image
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
                # TODO: fetch color names given hexcode maybe?
                st.write("The generated colors are: ",hex_colors)
            else:
                st.warning("👈🏼 Head over to the sidebar and click Generate!")    
    else:
        st.warning("👈🏼 Head over to the sidebar and upload an image!")    
    pass