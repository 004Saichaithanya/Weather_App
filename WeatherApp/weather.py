import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('YOUR_API_KEY')
print("API Key:", api_key)

st.title("🌤️ Weather Dashboard")

city = st.text_input("Enter a city name")

if st.button("Get Weather"):
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        print(url)
        response = requests.get(url)
        print(response)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            country = data['sys']['country']

            st.success(f"Weather in {data['name']}, {country}")
            st.write(f"**Temperature:** {temp} °C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Condition:** {description.title()}")
        else:
            st.error("City not found. Please check the name.")
    else:
        st.warning("Please enter a city name.")
