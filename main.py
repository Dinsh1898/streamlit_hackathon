import streamlit as st
import os
import json
import pandas as pd



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

# For now hard coding to create functionalities

#Initializing a variable
i=0

# Reading the input file
data = '[["What is the philosophy of handling status codes?", "The philosophy in handling status codes received on both Metro transaction formats is to distinguish the account condition from the payment state"], ["What does the system do with status codes?", "The system will translate incoming payment grids, payment rating codes, status codes, special comments (SCC1 and SCC2), and compliance condition codes into account condition(s) or payment state(s) or both"], ["What does the system keep a history of?", "The system will keep a history of all the account conditions and payment states reported for an account, regardless of whether they were reported via incoming payment grids, payment rating codes, status codes, special comments (SCC1 and SCC2), or compliance condition codes"], ["What does the system keep a history of?", "For audit purposes, the system will also keep a history of all the reported payment rating codes, status codes, special comments (SCC1 and SCC2), and compliance condition codes that were rejected by reason of failing the logical progression check or the reasonability check."], ["What can the TRU event perform?", "The TRU event can perform automated grid maintenance for M1RF reporters who report B2 or B3 segments on their monthly update tapes and for M2RF reporters who report payment history profiles"], ["How is the grid maintained?", "The Data Prep event passes the reported grid to the TRU event via the CCSSTRAD transaction\'s payment grid segment.\\nHistorical data on file that occurred before the time period covered by the payment grid segment is retained"], ["What is the manual request for the TRU event?", "If a reporter wants to correct account history that occurred prior to the time period covered in the payment grid segment, then the reporter must submit a manual request to Experian\'s Profile Maintenance department.\\nThe two reporter types that qualify for automated grid maintenance are:\\n\\t(1) Balance Reporter with Regular Payment Grid, and \\n\\t(2) Balance Reporter with History/B2/B3 Grid (M1RF only).\\nTo activate the automated grid maintenance process, the  user must set the appropriate Data Prep switch in the  database"], ["How does the Data Prep switch work?", "The Data Prep event passes this switch as a reporter processing option in the CCSSTRAD dataset\'s batch header record(s) - see section ."]]'
data_json = json.loads(data)
#Converting to pandas dataframe
data = pd.DataFrame(data_json)
data.columns = ['Question','Answer']
#Adding required columns
data['question_likes'] = 0
data['question_dislikes'] = 0
data['answer_likes'] = 0
data['answer_dislikes'] = 0


st.header('Question')
# Empty box
display_box = st.empty()

# Add outline to the box using markdown with border parameter
display_box.markdown(
    f'<div style="border: 1px solid #808080; padding: 10px; border-radius: 5px;">'
    f'{data["Question"].iloc[i]}'
    '</div>',
    unsafe_allow_html=True
)

# Thumbs up and thumbs down icons
thumbs_up_question = "👍"
thumbs_down_question = "👎"

# Display box with icons for question
col1, col2 = st.columns(2)

with col1:
    if st.button(thumbs_up_question + "-"):
        data['question_likes'].iloc[i]=data['question_likes'].iloc[i]+1
        st.write(data['question_likes'].iloc[i])

with col2:
    if st.button(thumbs_down_question + " ."):
        data['question_dislikes'].iloc[i]=data['question_likes'].iloc[i]+1
        st.write(data['question_dislikes'].iloc[i])


st.header('Answer')
# Empty box
display_box_ans = st.empty()

# Add outline to the box using markdown with border parameter
display_box_ans.markdown(
    '<div style="border: 1px solid #808080; padding: 10px; border-radius: 5px;">'
    f'{data["Answer"].iloc[i]}'
    '</div>',
    unsafe_allow_html=True
)

# Thumbs up and thumbs down icons
thumbs_up_answer = "👍"
thumbs_down_answer = "👎"

# Display box with icons for answer
col1_ans, col2_ans = st.columns(2)

if st.button(thumbs_up_answer):
        data['answer_likes'].iloc[i]=data['answer_likes'].iloc[i]+1
        st.write(data['answer_likes'].iloc[i])

with col2_ans:
    if st.button(thumbs_down_answer):
        data['answer_dislikes'].iloc[i]=data['answer_dislikes'].iloc[i]+1
        st.write(data['answer_dislikes'].iloc[i])

st.write("---")
# Next and Previous buttons
col_prev, col_next = st.columns(2)

prev_button = col_prev.button("Previous")
next_button = col_next.button("Next")

if prev_button:
    st.write("Previous button clicked")
    # The logic for going to the previous question and answer
    i -= 1
    st.write(i)

if next_button:
    st.write("Next button clicked")
    # The logic for going to the next question and answer
    i += 1
    st.write(i)

st.write(i)

st.write(data)