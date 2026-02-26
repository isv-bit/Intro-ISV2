import streamlit as st 
from PIL import Image 
st.title("Mi primera app")
st.header("Mucho gusto, Isabella.")

image = Image.open("Nala.JPEG")
st.image(image, caption = "Esta es mi mascota")
texto = st.text_input ("Imagen texto"," texto inicial")
st.write("El texto que has escrito es", texto)
