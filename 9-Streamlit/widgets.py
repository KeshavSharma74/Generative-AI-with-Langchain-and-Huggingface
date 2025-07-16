import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name")

age=st.slider("Enter your age : ",0,100,25)
st.write(age)

options=["C++","Python","Java","Rust","C#","C"]
choice=st.selectbox("Select your favourite Language : ",options)
st.write("You Selected : ",choice)

data={
    "UID":["21BCS9472","21BCS9426","21BCS9614","21BCS9453"],
    "Name":["Keshav Sharma","Chetan Rao","Shubham","Anil Kumar"],
    "Marks":["97","100","98","99"]
}

df=pd.DataFrame(data)
st.write(df)

file_upload=st.file_uploader("Choose a CSV File",type="csv")

if(file_upload):
    df=pd.read_csv(file_upload)
    st.write(df)

if name:
    st.write(f"Hello {name}")