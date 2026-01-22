import streamlit as st
import requests

st.title("Something")
name = st.text_input("Name:")
if st.button("Check"):
  if name.strip() == "":
    st.warning("Please enter text:")
  elif not name.isalpha():
    st.warning("      ")
  else:
    st.success("The text is correct")

