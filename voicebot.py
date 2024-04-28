import streamlit as st
import openai
from audiorecorder import audiorecorder

print(f"streamlit {st.__version__}")

def TTS():
    pass

def ask_gpt():
    pass

def STT():
    pass

def main():
    st.set_page_config(page_title="Voice Bot ver 0.1", layout='wide')

    st.header("Voice Bot")

    st.markdown("---")

    with st.expander("Voice Bot에 대해...", expanded=True):
        st.write("""     
        - 음성비서 프로그램의 UI는 스트림릿을 활용했습니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper AI를 활용했습니다. 
        - 답변은 OpenAI의 GPT 모델을 활용했습니다. 
        - TTS(Text-To-Speech)는 구글의 Google Translate TTS를 활용했습니다.
        """)

    st.markdown("")

    with st.sidebar:

        # openai 0.28
        openai.api_key = st.text_input(label="OPENAI API 키", 
                                                       placeholder="Enter Your API Key", 
                                                       value="", type="password")
        st.markdown("---")
        model = st.radio(label="GPT 모델",
                         options=["gpt-4", "gpt-3.5-turbo"])
        st.markdown("---")

        if st.button(label='초기화'):
            st.session_state['chat'] = []
            st.session_state['messages'] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
            st.session_state['check_reset'] = True

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("질문하기")
        audio = audiorecorder()
        if (audio.duration_seconds > 0) and \
            (st.session_state['check_reset'] == False):
            st.audio(audio.export().read())

        

    with col2:
        st.subheader("질문/답변")

if __name__ == '__main__':
    main()