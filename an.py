import streamlit as st
import os

k=open("sample.txt","r")
st.header("give proper indentation(proper spacing)")
for line in k:
    st.write(line)
k.close()