from transformers import pipeline
import streamlit as st

# Streamlite 
st.title('Automated Storyteller')

max_length = st.selectbox(
    'How long do you want the story to be?',
    [50, 100, 200, 400]
)

input_text = st.text_input(
    label='Write a beggining to the story...',
)

# Text generator
text_generator = pipeline("text-generation")

generated_text = text_generator(input_text, max_length=max_length, do_sample=True)[0][
    "generated_text"
]

# use this code for testing/eval/any problems with the one above.
#generated_text = text_generator('Shalom!', max_length=1023, do_sample=True)[0][
#    "generated_text"
#]

st.write(generated_text)
