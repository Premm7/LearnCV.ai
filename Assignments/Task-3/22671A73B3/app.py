import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="Image Processing Toolkit", layout="wide")

st.title("📸 Image Processing & Analysis Toolkit")

# Sidebar for uploading image

uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.sidebar.success("Image Uploaded Successfully!")

    

    # Choose operation

    option = st.sidebar.selectbox("Select Operation", [

        "Show Image Info", "Grayscale", "HSV", "YCbCr",

        "Rotate", "Resize", "Translate", "Canny Edge Detection"

    ])

    

    processed_img = img_rgb.copy()

    if option == "Show Image Info":

        st.sidebar.write(f"Shape: {img.shape}")

        st.sidebar.write(f"Dimensions: {img.shape[0]}x{img.shape[1]}")

    elif option == "Grayscale":

        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    elif option == "HSV":

        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    elif option == "YCbCr":

        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    elif option == "Rotate":

        angle = st.sidebar.slider("Rotation Angle", -180, 180, 45)

        (h, w) = img.shape[:2]

        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)

        processed_img = cv2.warpAffine(img_rgb, M, (w, h))

    elif option == "Resize":

        scale = st.sidebar.slider("Scaling Factor", 10, 200, 100)/100

        processed_img = cv2.resize(img_rgb, None, fx=scale, fy=scale)

    elif option == "Translate":

        tx = st.sidebar.slider("Shift X", -100, 100, 20)

        ty = st.sidebar.slider("Shift Y", -100, 100, 20)

        M = np.float32([[1,0,tx],[0,1,ty]])

        processed_img = cv2.warpAffine(img_rgb, M, (img.shape[1], img.shape[0]))

    elif option == "Canny Edge Detection":

        t1 = st.sidebar.slider("Threshold1", 0, 500, 100)

        t2 = st.sidebar.slider("Threshold2", 0, 500, 200)

        processed_img = cv2.Canny(img, t1, t2)



    col1, col2 = st.columns(2)

    with col1:

        st.image(img_rgb, caption="Original Image")

    with col2:

        st.image(processed_img, caption=f"Processed Image - {option}")
