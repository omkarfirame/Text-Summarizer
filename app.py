import streamlit as st
from textSumarizer.pipeline.prediction import PredictionPipeline

# Load your custom summarization model
model = PredictionPipeline()

# Streamlit app
def main():
    st.title("Text Summarization API")

    # User input for text
    user_input = st.text_area("Enter the text you want to summarize:")

    if st.button("Generate Summary"):
        # Check if user input is not empty
        if user_input:
            # Use your custom model to generate a summary
            summary = model.predict(user_input)

            # Display the original text and the generated summary
            st.subheader("Original Text:")
            st.write(user_input)

            st.subheader("Generated Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()
