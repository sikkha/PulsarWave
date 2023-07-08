import streamlit as st

def count_words(input_text):
    words = input_text.split(' ')
    num_words = len(words)
    return num_words

st.title('Word Count App')

user_input = st.text_input('Enter some text')
if st.button('Count Words'):
    word_count = count_words(user_input)
    st.write(f'The text contains {word_count} words.')

