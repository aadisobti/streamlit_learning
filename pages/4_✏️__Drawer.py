import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import time

# Set up the page
st.set_page_config(page_title="Drawing Canvas", page_icon="🖌️")

# List of items to draw
items_to_draw = ["cat", "dog", "house", "tree", "car", "flower", "sun", "star"]

# Select a random item
item_to_draw = random.choice(items_to_draw)
st.markdown(f"## Draw a **{item_to_draw}**")

# Sidebar options
stroke_width = st.sidebar.slider("Stroke width:", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color:", "#000000")
bg_color = st.sidebar.color_picker("Background color:", "#FFFFFF")

# Timer settings
draw_time = 10  # Set the timer in seconds

if "timer_started" not in st.session_state:
    st.session_state.timer_started = False
    st.session_state.start_time = None
    st.session_state.canvas_image = None
    st.session_state.time_left = draw_time

def start_timer():
    st.session_state.timer_started = True
    st.session_state.start_time = time.time()
    st.session_state.time_left = draw_time

# Button to start the timer
if st.sidebar.button("Start Timer"):
    start_timer()

# Timer display
timer_placeholder = st.empty()

# Show canvas only if the timer has started
if st.session_state.timer_started and st.session_state.time_left > 0:
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        update_streamlit=True,
        height=400,
        drawing_mode="freedraw",  # Only freedraw tool
        key="canvas"
    )

# Update the timer
if st.session_state.timer_started:
    while st.session_state.time_left > 0:
        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.time_left = max(0, draw_time - int(elapsed_time))
        timer_placeholder.markdown(f"<h3>Time left: {st.session_state.time_left}</h3>", unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.timer_started = False
    # Save the canvas image after the timer ends
    if 'canvas_result' in locals() and canvas_result.image_data is not None:
        st.session_state.canvas_image = canvas_result.image_data

# Display saved drawing if timer is not running
if not st.session_state.timer_started and st.session_state.canvas_image is not None:
    st.image(st.session_state.canvas_image, use_column_width=True)

# Button to clear the canvas
if st.sidebar.button("Clear Canvas"):
    st.session_state.timer_started = False
    st.session_state.canvas_image = None
    st.experimental_rerun()

# Button to save the drawing
if st.sidebar.button("Save Drawing"):
    if st.session_state.canvas_image is not None:
        st.write("Drawing saved!")  # Here you can add code to save the drawing
    else:
        st.write("No drawing to save.")
