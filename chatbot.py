# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("AIzaSyDlkm2O5f7aujVl__OZEf3j50lP0HK4vnE")
genai.configure(api_key="AIzaSyDlkm2O5f7aujVl__OZEf3j50lP0HK4vnE")

## Function to load OpenAI model and get respones
s=""
x=0
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app
st.set_page_config(layout="wide")

con="""Abhishek: Good afternoon, Officer. I'm Abhishek Roy, and I need to report a theft that occurred during my journey from New Delhi to Jalandhar on the Paschim Express.

Police Officer: Good afternoon, Mr. Roy. I'm Officer Sharma. I'm here to assist you. Please, have a seat. Could you provide me with all the details regarding the incident?

Abhishek: Certainly, Officer Sharma. So, while I was traveling on the Paschim Express, I realized that my luggage had been stolen.

Police Officer: I see. Can you tell me when you first noticed that your luggage was missing?

Abhishek: Yes, I realized it was missing shortly after we departed from New Delhi station. I had stored my luggage in the overhead compartment of the train. But when I went to retrieve it later, it was nowhere to be found.

Police Officer: Did you notice anyone acting suspiciously or any unusual activity during the journey?

Abhishek: No, Officer. I didn't observe anything out of the ordinary. It seems like the theft must have occurred when I momentarily left my seat.

Police Officer: Alright. Can you provide me with a detailed description of your luggage? Any distinctive features or items inside that could help us identify it?

Abhishek: Certainly. It's a black suitcase with a red stripe along the side. Inside, there are mainly clothes, toiletries, and some personal items. Additionally, I had my laptop, a few pieces of jewelry, and important documents like my passport and ID card in the suitcase.

Police Officer: Thank you for the detailed description, Mr. Roy. We'll make sure to include all these items in the report. Did you notice any specific individuals or groups behaving suspiciously in the vicinity of your seat or the overhead compartment?

Abhishek: No, Officer. I didn't notice anything unusual or any suspicious individuals around me during the journey.

Police Officer: Understood. We'll need you to fill out a formal report with all these details. Additionally, we'll conduct further investigations and check CCTV footage if available. Please come with me to the station, and we'll get started on the process.

Abhishek: Thank you, Officer Sharma. I really appreciate your assistance in this matter.

Police Officer: You're welcome, Mr. Roy. We'll do everything in our power to recover your belongings. Let's head to the station and get the report filed."""
st.header("Fir-Registration")
input=st.text_input("Enter your queery: ",key="input")
placeholder1=st.empty()
col1, col2 ,col3,col4 ,col5= st.columns(5)
with col1:
    if st.button("search"):
        s = get_gemini_response(input)
with col2:
    if st.button("Genrate Fir"):
        input="This is ureser issue and you want to convert it into "+con+" fir formate "+ "FIR Registration Form Complainant Details: Name of Complainant: [Fill in your full name] Gender: [Fill in your gender: Male / Female / Other] Date of Birth: [Fill in your date of birth] Address: [Fill in your address] Contact Number: [Fill in your contact number] Email Address: [Fill in your email address (if available)] Incident Details: Date and Time of Incident: [Fill in date and time of incident] Location of Incident: [Fill in location of incident] Type of Incident: [Fill in type of incident: Theft / Assault / Fraud / Other] Description of Incident: [Provide a detailed description of the incident] Accused Details (if known): Name of Accused: [Fill in name of accused (if known)] Description of Accused: [Provide description of accused (if available)] Identifying Information: [Any additional identifying information] Witness Information (if any): Name of Witness: [Fill in name of witness (if any)] Contact Information of Witness: [Fill in contact information of witness (if available)] Witness Statement: [Provide statement of witness (if available)] Evidence (if available): Upload Documents/Photos/Videos: [Attach any relevant evidence files] Additional Information: [Provide any additional details or comments related to the incident] Declaration: I hereby declare that the information provided above is true and accurate to the best of my knowledge and belief. Signature (Digital Signature):[Use your mouse or touchscreen to sign below] Date and Time of Submission: [Automatically captured date and time]"
        s=get_gemini_response(input)
with col3:
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file)


with col4:
    pass
with col5:
    option = st.selectbox(
        'language',
        ('English', 'Hindi', 'Telgue')
    )


st.write(s)

