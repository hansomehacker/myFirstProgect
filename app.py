import streamlit as st

st.title("My first project ever")
name = st.text_input("Name:")

if name:
  st.write("hello ", name, "!")
  
