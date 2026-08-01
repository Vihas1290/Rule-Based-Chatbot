import streamlit as st
from edgefil import interactive_edge_detection, display_image

st.title("Photo Editing Application")

if st.button("Start Edge Detection"):
    image_path = st.text_input("Enter the path to the image:")
    if image_path:
        interactive_edge_detection(image_path)
    else:
        st.warning("Please enter a valid image path.")