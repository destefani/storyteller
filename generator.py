from transformers import pipeline

INPUT_TEXT = "As far as I am concerned, I will"
MAX_LENGHT = 50

text_generator = pipeline("text-generation")

generated_text = text_generator(INPUT_TEXT, max_length=MAX_LENGHT, do_sample=False)[0][
    "generated_text"
]
