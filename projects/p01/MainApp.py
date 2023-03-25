import streamlit as st
import cv2
import numpy as np
'''
Image Editor Functionalities
    - Resize Image
    - Crop Image
    - Add Text
    - Rotate Flip
    - Vignette
    - Background Removal
    - Generate Color FIlter
    - Apply Filters
'''
def resizeImage(orig_img,resize_img=None):
    st.markdown("### 📏 Resize Image")
    if resize_img is None:
        resize_img = orig_img
    img_resize_options = (
        "By Pixels",
        "By Percentage"
    )
    img_resize_opt = st.radio(
        "Resize Options",
        img_resize_options
    )
    orig_img_size = orig_img.shape
    orig_img_w = orig_img_size[1]
    orig_img_h = orig_img_size[0]
    if img_resize_opt == img_resize_options[0]:
        resize_config_cols = st.columns([2,1,1,6])
        with resize_config_cols[0]:
            is_exact_size = st.checkbox("Maintain Aspect Ratio",value=True)
        with resize_config_cols[1]:
            resize_width = int(st.number_input(
                "Width (px):",
                min_value=int(10), 
                max_value=int(orig_img_w*10), 
                value=int(orig_img_w)))
        if not is_exact_size:
            with resize_config_cols[2]:
                resize_height = int(st.number_input(
                    "Height (px):",
                    min_value=int(10), 
                    max_value=int(orig_img_h*10), 
                    value=int(orig_img_h)))
        else:
            resize_height = int(orig_img_h * (resize_width/orig_img_w))
        if resize_width and resize_height:
            resize_img = cv2.resize(
                orig_img,
                (resize_width,resize_height)
            )
        pass
    elif img_resize_opt == img_resize_options[1]:
        resize_config_cols = st.columns([2,1,1,6])
        with resize_config_cols[0]:
            is_exact_size = st.checkbox("Maintain Aspect Ratio",value=True)
            # aspect_ratio =["1:1", "16:9", "4:3", "2:3", "Free"]
        with resize_config_cols[1]:
            resize_width_percent = int(st.number_input(
                "Width (%):",
                min_value=int(10), 
                max_value=int(100*10), 
                value=int(100)))
            resize_width = int(orig_img_w*resize_width_percent/100)
        if not is_exact_size:
            with resize_config_cols[2]:
                resize_height_percent = int(st.number_input(
                    "Height (%):",
                    min_value=int(10), 
                    max_value=int(100*10), 
                    value=int(100)))
                resize_height = int(orig_img_h*resize_height_percent/100)
        else:
            resize_height = int(orig_img_h*resize_width_percent/100)
        if resize_width and resize_height:
            resize_img = cv2.resize(
                orig_img,
                (resize_width,resize_height)
            )
        pass
    img_cols = st.columns(2)
    with img_cols[0]:
        st.image(orig_img, caption=f"W:{orig_img_w} | H:{orig_img_h}")
    with img_cols[1]:
        resize_img_size = resize_img.shape
        st.image(resize_img, caption=f"W:{resize_img_size[1]} | H:{resize_img_size[0]}")
    pass
def cropImage(orig_img):
    st.markdown("### ✂️ Crop Image")
    pass
def App():
    uploaded_img = st.file_uploader("Choose an Image", type=["png", "jpg", "jpeg"])
    if uploaded_img is not None:
        with st.sidebar:
            img_edit_options = (
                'Resize'
                ,'Crop'
                )
            img_edit_opt = st.radio(
                "So what do you wanna do with the image?",
                img_edit_options
            )
        # https://github.com/streamlit/streamlit/issues/888
        file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
        cv_orig_img = cv2.cvtColor(cv2.imdecode(file_bytes, 1), cv2.COLOR_BGR2RGB)
        st.info("Choose Image Editing Options from side bar..",icon="👈")
        if img_edit_opt == img_edit_options[0]:
            resizeImage(cv_orig_img)
        elif img_edit_opt == img_edit_options[1]:
            cropImage(cv_orig_img)
    pass
