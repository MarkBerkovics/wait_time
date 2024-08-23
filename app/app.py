import streamlit as st
import matplotlib.image as mpimg
import requests

st.markdown("# Customer service wait time calculator")
st.markdown("### Just enter the day of the week and time of the day and get your wait time estimation")

day = st.number_input("Enter a day of the week", min_value=1, max_value=7)
time = st.number_input("Enter a time of the day", min_value=1, max_value=24)
# st.image(mpimg.imread('raw_data/upset-person-on-phone-760.jpg'))

url = "http://127.0.0.1:8000/predict"
params = {
    "day_of_week": day,
    "time_of_day": time
}

response = requests.get(url, params).json()
answer = f"Your wait time is: {response['Minutes to wait']} minutes"

if st.button("Calculate"):
    st.write(answer)
    st.image(mpimg.imread('raw_data/upset-person-on-phone-760.jpg'))
