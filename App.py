import streamlit as st
import streamlit.components.v1 as components


st.markdown(
    "<h1 style='text-align: center;'>Image Creator</h1>",
    unsafe_allow_html=True
)

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
