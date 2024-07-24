import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Weather Data", page_icon="🌤️")
st.markdown("# Weather Data")
st.sidebar.header("Weather Data")


api_key = "D4RYZBAFPLZ9EECPW5Z7RPTHX"
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# Input
location = st.sidebar.text_input("Enter a location:", "New York")

encoded_location = requests.utils.quote(location)

url = f"{base_url}{encoded_location}?key={api_key}"

@st.cache_data
def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

data_load_state = st.text('Loading data...')
weather_data = fetch_weather_data(url)
data_load_state.text("Done!")

if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(weather_data)

if weather_data:
    st.subheader(f"Weather Data for {location}")

    days = weather_data['days']
    dates = [day['datetime'] for day in days]
    temps = [day['temp'] for day in days]

    df = pd.DataFrame({
        'Date': dates,
        'Temperature': temps
    })

    st.line_chart(df.set_index('Date'))

    today = weather_data['days'][0]
    st.write(f"**Summary for today:** {today['description']}")
    st.write(f"**Temperature:** {today['temp']}°C")
    st.write(f"**Humidity:** {today['humidity']}%")
    st.write(f"**Wind Speed:** {today['windspeed']} km/h")

if st.button("Re-fetch Data"):
    st.experimental_rerun()
