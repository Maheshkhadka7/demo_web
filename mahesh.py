import streamlit as st
import pandas as pd

st.title("Admission Form")
st.subheader("Please Fill All And Press On Submit Button")
hi=st.warning("YOU ARE NOT ALLOWED TO SUBMIT WITH INCORRECT DATA")
name=st.text_input("Enter Your Full Name: ")
home=st.camera_input("TAKE YOUR PICTURE")
date= st.date_input("Enter The Date Of Form Filled:")
email= st.text_input("Enter Your Contact Number:")
fname=st.text_input("Enter Your Father's name:")
mname=st.text_input("Enter Your Mother's name:")
address=st.text_input("Enter Your Address:")
adr=st.text_area("Why did you choose us??")
classdata= st.selectbox("Enter Your Class:",(8,9,10,11,12))

butt= st.button("Submit")
if butt:
    st.success('Your admission form has been recorded.')
    st.markdown(f""" 
  Name: {name}
  Form Was Filled On:{date}
  Contact: {email}
Father's Name: {fname}
Mother's Name: {mname}
Address: {address}
Why did you choose us!!: {adr}
Class: {classdata}""")