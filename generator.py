from transformers import pipeline
import streamlit as st
import numpy as np
import pandas as pd

st.title('Automated Storyteller')


INPUT_TEXT = "As far as I am concerned, I will"
MAX_LENGHT = 50

text_generator = pipeline("text-generation")

generated_text = text_generator(INPUT_TEXT, max_length=MAX_LENGHT, do_sample=False)[0][
    "generated_text"
]

st.write(generated_text)

