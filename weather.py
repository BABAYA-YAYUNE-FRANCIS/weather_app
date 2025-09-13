import streamlit as st
import requests

def get_weather(city):
    url = f"http://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            weather_info = {
                "Temperature (°C)": current['temp_C'],
                "Feels Like (°C)": current['FeelsLikeC'],
                "Weather": current['weatherDesc'][0]['value'],
                "Humidity (%)": current['humidity'],
                "Wind (km/h)": current['windspeedKmph'],
            }
            return weather_info
        else:
            return None
    except Exception as e:
        return None

# Streamlit UI
st.set_page_config(page_title="Weather Checker", page_icon="⛅")
st.title("🌤️ Weather Checker")
st.write("Enter a city name to get the current weather:")

city = st.text_input("City Name")

if city:
    st.write(f"Fetching weather for **{city}**...")
    weather = get_weather(city)
    
    if weather:
        st.success("Current Weather:")
        for key, value in weather.items():
            st.write(f"**{key}:** {value}")
    else:
        st.error("Could not fetch weather data. Please check the city name or try again later.")
