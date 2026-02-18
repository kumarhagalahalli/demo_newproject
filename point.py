import streamlit as st
import pandas as pd

st.title("Welcome to RRK Website Tech")
st.header("Python")
st.subheader("Java")
st.markdown("I Love Rithvi")
st.code(""" for i in range (1,5,1):
    print("Hello")
""")

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your fname : ")
adr = st.text_area("Enter Your Address : ")
classdata =st.selectbox("Enter Your Class :", (1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
""")
