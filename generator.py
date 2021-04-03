from transformers import pipeline
import streamlit as st

# Streamlite 
st.title('Automated Storyteller')
st.write('This is Machine Learning based automatic story generator.\
          For a story to be generated you have to specify the number of words the story to have,\
          and write the start of the story. Remember that the longer the story the longer it will takte to be generated')

max_lenght = st.selectbox(
    'How long do you want the story to be?',
    [50, 100]
)

input_text = st.text_input(
    label='Write a beginning to the story...',
)

# Text generator
if input_text:
    text_generator = pipeline("text-generation")

    generated_text = text_generator(input_text, max_length=max_lenght, do_sample=True)[0][
        "generated_text"
    ]

    st.write(generated_text)

