import streamlit as st
from PIL import Image


st.title("Página de Inicio")
st.header("Desde ésta página puedes controlar el funcionamiento de tu casa")
image=Image.open("CasaObraBlanca.jpeg")
st.image(image, caption= "Ésta es la casa")


st.subheader("Ahora Usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto") 
with col2:
  st.subheader("Esta es la segunda")
  modo=st.radio("Que modalidad es la principal de tu interfaz",("Visual", "auditivo", "tactil"))
  if modo=="Visual":
    st.write("lA VISTA ES FUNDAMENTAL PARA TU INTERFAZ")
  if modo=="auditivo":
    st.write("skjasjdklas")
  if modo=="tactil":
    st.write("jdasdlaksdadoj")
