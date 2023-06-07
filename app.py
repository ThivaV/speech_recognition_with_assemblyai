import assemblyai as aai
import streamlit as st


def main() -> None:
    """main function for extract the audio sentences"""

    with st.form("AssemblyAI Key Form"):
        with st.container():
            aai_key = st.text_input("Enter the AssemblyAI Key", type="password")

            audio_file_path = st.text_input("Enter audio file path")

            submitted = st.form_submit_button("Start Transcribe")

            if aai_key and audio_file_path and submitted:
                progress_text = "Operation in progress. Please wait."
                progress_bar = st.progress(0, text=progress_text)
                percent_complete = 10

                progress_bar.progress(percent_complete, text=progress_text)

                # load aai keys
                aai.settings.api_key = aai_key

                # transcribe files
                transcriber = aai.Transcriber()
                transcript = transcriber.transcribe(audio_file_path)

                percent_complete = percent_complete + 30
                progress_bar.progress(percent_complete + 30, text=progress_text)

                st.write("Audio duration: ", transcript.audio_duration, " seconds")

                # print all at once
                with st.expander("Audio transcript as in a paragraph"):
                    st.write(transcript.text)
                    percent_complete = percent_complete + 20
                    progress_bar.progress(percent_complete, text=progress_text)

                # get sentences
                with st.expander("Audio transcript as in sentences"):
                    sentences = transcript.get_sentences()
                    for sentence in sentences:
                        st.write(sentence.text)

                    percent_complete = percent_complete + 20
                    progress_bar.progress(percent_complete, text=progress_text)

                # get paragraphs
                with st.expander("Audio transcript as in paragraphs"):
                    paragraphs = transcript.get_paragraphs()
                    for paragraph in paragraphs:
                        st.write(paragraph.text)

                    progress_bar.progress(100, text=progress_text)


if __name__ == "__main__":
    st.title(":blue[Speech Recognition] :sunglasses:")

    st.image("./img/speech_recognition.png")
    st.header("Speech Recognition with AssemblyAI")

    st.info(
        """
    * Please enter the AssemblyAI Key
    * Upload the audio file"""
    )

    main()
