import streamlit as st
from text_generator import text_generator

def main():
    st.title('Automated Storyteller')
    st.write('This is a Machine Learning based automatic story generator.\
            For a story to be generated you have to specify the number of words the story to have\
            and write the start of it. Remember that the longer the story the longer it will takte to be generated')

    max_lenght = st.selectbox(
        'How long do you want the story to be?',
        [50, 100]
    )

    input_text = st.text_input(
        label='Write a beginning to your story...',
    )

    # Text generator
    if input_text:
        generated_text = text_generator(input_text, max_lenght=max_lenght, do_sample=True)[0][
            "generated_text"
        ]

        st.write(generated_text)

if __name__ == '__main__':
    main()

