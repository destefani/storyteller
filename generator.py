from transformers import pipeline
import streamlit as st

# Streamlite 
st.title('Automated Storyteller')

max_lenght = st.selectbox(
    'How long do you want the story to be?',
    [50, 100, 200, 400]
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

