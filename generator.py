import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyAp2pOQwlCHMKe3VJ0OSzmolLXVeDpPHF4'

def embed_watermark(text):
    watermark_pattern = ['\u200B', '\u200C', '\u200D', '\uFEFF']
    words = text.split()
    watermarked_text = ""
    for i, word in enumerate(words):
        space = watermark_pattern[i % len(watermark_pattern)]
        watermarked_text += word + space + ' '
    return watermarked_text

def main():
    st.title("Watermarked Text Generator")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = st.text_input("Enter your prompt:")

    if st.button("Generate and Watermark"):
        if prompt:
            response = model.generate_content(prompt)
            watermarked_text = embed_watermark(response.text)
            st.write("Watermarked Text:")
            st.write(watermarked_text)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()