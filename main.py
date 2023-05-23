import streamlit as st
import os

st.markdown('''
# Transform Pre-existing Grammars
''')

def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    return files

# Folder path
folder_path = "data"

# Get file names in the folder
files = list_files_in_folder(folder_path)

# File dropdown
selected_file = st.sidebar.selectbox("Select a file", files)

uploaded_files = st.sidebar.file_uploader("OR Upload a file(s)", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.header('Question')
# Empty box
display_box = st.empty()

# Add outline to the box using markdown with border parameter
display_box.markdown(
    '<div style="border: 1px solid #808080; padding: 10px; border-radius: 5px;">'
    'This is a box for question.'
    '</div>',
    unsafe_allow_html=True
)

# Thumbs up and thumbs down icons
thumbs_up = "👍"
thumbs_down = "👎"

# Display box with icons for question
col1, col2 = st.columns(2)

with col1:
    if st.button(thumbs_up + " ."):
        display_box.success("You clicked thumbs up!")

with col2:
    if st.button(thumbs_down + " ."):
        display_box.error("You clicked thumbs down!")


st.header('Answer')
# Empty box
display_box_ans = st.empty()

# Add outline to the box using markdown with border parameter
display_box_ans.markdown(
    '<div style="border: 1px solid #808080; padding: 10px; border-radius: 5px;">'
    'This is a box for answer.'
    '</div>',
    unsafe_allow_html=True
)

# Display box with icons for answer
col1_ans, col2_ans = st.columns(2)

with col1_ans:
    if st.button(thumbs_up):
        display_box_ans.success("You clicked thumbs up!")

with col2_ans:
    if st.button(thumbs_down):
        display_box_ans.error("You clicked thumbs down!")

st.write("---")
# Next and Previous buttons
col_prev, col_next = st.columns(2)

prev_button = col_prev.button("Previous")
next_button = col_next.button("Next")

if prev_button:
    st.write("Previous button clicked")
    # Add your logic for going to the previous question or answer here

if next_button:
    st.write("Next button clicked")
    # Add your logic for going to the next question or answer