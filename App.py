import streamlit as st
import streamlit.components.v1 as components


# Title for the Streamlit app
st.title("Image Creator")

# Embedding the iframe
components.html(
    """
    <iframe
        src="https://vismaya2939-texttoimage.hf.space"
        frameborder="0"
        width="850"
        height="450"
    ></iframe>
    """,
    height=500,  # Set the height of the iframe container
)
