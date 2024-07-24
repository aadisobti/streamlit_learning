import streamlit as st

st.set_page_config(page_title="About Me", page_icon="📈")

st.markdown("""
    <style>
        .main {
            background: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs9gKZOQtPuPqNqtv4Sznwxk1FbV7qimmPOw&s');
            background-size: cover;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #FFA500;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("# About Me")
st.sidebar.header("About Me")
st.write(
    """
    Hi, I'm Aadi Sobti. I'm passionate about app development and creating innovative solutions.
    Currently, I'm working on an iOS app called FireWatch, which helps users stay informed about wildfires and provides safety tips.
    
    ### Skills
    - iOS Development
    - Python Programming
    - Machine Learning
    - Data Analysis

    ### Projects
    - **FireWatch App**: An iOS app for wildfire safety and updates.
    - **WeatherWatch**: Integrating weather data into apps using Visual Crossing Weather API.
    
    ### Hobbies
    - Coding
    - Hiking
    - Reading

    Feel free to connect with me on my journey to develop impactful apps!
    """
)

st.markdown("""
    <div>
        <img src="https://pbs.twimg.com/profile_images/326978888/iPhone_029_400x400.JPG" alt="Kid pic" style="margin: 10px;;width: 300px;">
        <img src="https://media.licdn.com/dms/image/D5603AQGxkUjzo1xjvw/profile-displayphoto-shrink_200_200/0/1718286622069?e=2147483647&v=beta&t=KD5Ia7e0PA81NCUawRNePB18Vas4T8WaL55t9IY4ITk" alt="Profile" style="margin: 10px;width: 300px;">
    </div>
""", unsafe_allow_html=True)

st.sidebar.write(
    """
    ### Connect with me
    - [LinkedIn](https://www.linkedin.com)
    - [GitHub](https://github.com)
    - [Twitter](https://twitter.com)
    """
)
