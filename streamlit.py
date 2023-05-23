import streamlit as st
import json
import os
from datetime import datetime

st.markdown('''
# Transform Pre-existing Grammars
''')

if 'idx' not in st.session_state:
    st.session_state.idx = 0

if 'worklist' not in st.session_state:
    st.session_state.worklist = []

if 'wlen' not in st.session_state:
    st.session_state.wlen = 0

if 'response' not in st.session_state:
    st.session_state.response = [0, 0, st.session_state.idx]

if 'responses' not in st.session_state:
    st.session_state.responses = [[] for _ in range(50)]

cwd = os.getcwd()


def main():
    # Folder path
    folder_path = "data"

    # Get file names in the folder
    files = list_files_in_folder(folder_path)

    # File dropdown
    selected_file = st.sidebar.selectbox("Select a file", files)
    loadFilesToWorklist('/'.join([cwd, folder_path, selected_file]))

    # Next and Previous buttons
    st.write('{}/{}'.format(st.session_state.idx+1, st.session_state.wlen))
    col_prev, col_next, col_submit = st.columns(3)

    prev_button = col_prev.button("Previous")
    next_button = col_next.button("Next")
    submit_button = col_submit.button("Submit")

    if prev_button:
        st.session_state.responses[st.session_state.idx] = st.session_state.response
        st.session_state.idx -= 1
        st.session_state.idx = max(0, st.session_state.idx)
        st.session_state.response = [0, 0, st.session_state.idx]

        # Add your logic for going to the previous question or answer here

    if next_button:
        st.session_state.responses[st.session_state.idx] = st.session_state.response
        st.session_state.idx += 1
        st.session_state.idx = min(st.session_state.wlen - 1, st.session_state.idx)
        st.session_state.response = [0, 0, st.session_state.idx]
        # Add your logic for going to the next question or answer

    if submit_button:
        ts = datetime.now().strftime('%m%d%Y%H%M%S"')
        fileout = '/'.join([cwd, folder_path, 'output/{}-{}'.format(selected_file, ts)])
        print(st.session_state.responses)
        temp = json.dumps(st.session_state.responses[:st.session_state.wlen])
        with open(fileout,'w') as fp:
            fp.write(temp)

    st.header('Question')
    # Empty box
    display_box = st.empty()
    question = st.session_state.worklist[st.session_state.idx][0]

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
    display_box.write(question)
    col1, col2 = st.columns(2)

    with col1:
        if st.button(thumbs_up + " ."):
            st.session_state.response[0] = 1

    with col2:
        if st.button(thumbs_down + " ."):
            st.session_state.response[0] = -1

    if st.session_state.response[0] == 1:
        display_box.success(question)
    elif st.session_state.response[0] == -1:
        display_box.error(question)

    st.header('Answer')
    # Empty box
    display_box_ans = st.empty()
    answer = st.session_state.worklist[st.session_state.idx][1]

    # Add outline to the box using markdown with border parameter
    display_box_ans.markdown(
        '<div style="border: 1px solid #808080; padding: 10px; border-radius: 5px;">'
        'This is a box for answer.'
        '</div>',
        unsafe_allow_html=True
    )

    # Display box with icons for answer
    col1_ans, col2_ans = st.columns(2)
    display_box_ans.write(answer)
    with col1_ans:
        if st.button(thumbs_up):
            st.session_state.response[1] = 1

    with col2_ans:
        if st.button(thumbs_down):
            st.session_state.response[1] = -1

    if st.session_state.response[1] == 1:
        display_box_ans.success(answer)
    elif st.session_state.response[1] == -1:
        display_box_ans.error(answer)

    st.write("---")


def list_files_in_folder(folder_path):
    files = [x for x in os.listdir(folder_path) if x.lower() not in ['.ds_store']]
    return files


def loadFilesToWorklist(filename):
    with open(filename, 'r') as fp:
        st.session_state.worklist = json.load(fp)
    st.session_state.wlen = len(st.session_state.worklist)


if __name__ == '__main__':
    main()
