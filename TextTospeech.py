import streamlit as st
import pyttsx3
import time


st.set_page_config(
    page_title="Text To speeach",
    page_icon="📑",
    layout="centered"
)

class VoiceModel:
    
    def MaleVoice(self,Voice:str):  #######  male voice
        try:
            self.Voice = Voice
            MaleEngine = pyttsx3.init()
            MaleEngine.say(Voice)
            MaleEngine.runAndWait()
            MaleEngine.stop()
        except:
            st.warning("Something went wrong")

    def FemaleVoice(self,Voice:str):  ##### female voice
        try:
           self.Voice = Voice
           FemaleEngine = pyttsx3.init()
           Fvoice = FemaleEngine.getProperty("voices")
           FemaleEngine.setProperty("voice",Fvoice[1].id)
           FemaleEngine.say(Voice)
           FemaleEngine.runAndWait()
           FemaleEngine.stop()
        except:
            st.warning("Something went wrong")

st.header("Test to Speech")


TextInput = st.text_area(
    label="Enter Text",   #####  text input
    height=260,
    placeholder="Write Something"
)

Mybar = st.progress(0,text="")
for i in range(100):
    time.sleep(0.002)
    Mybar.progress(i+1,text="")

Models = st.radio(
    label="Select Voice Model",
    options=["Male","Female"],
    horizontal=True
)

model = VoiceModel()

if Models == "Male":
    try:
        st.toast("Male Model",icon="👨‍🦰")
        maleVoice = model.MaleVoice(TextInput)
        st.button("Speak",on_click=maleVoice)
    except:
        st.warning("Something went wrong")

if Models == "Female":
    try:
        st.toast("Female Model",icon="👩‍🦰")
        femalevoice = model.FemaleVoice(TextInput)
        st.button("Speak",on_click=femalevoice)
    except:
        st.warning("Something went wrong")