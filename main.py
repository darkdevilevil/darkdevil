
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["api"])
def ai(txt):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    data= results.generate_content("from now your name is darkdevil and your a ethical hacker,fullstack developer,cooking,mobile enthusiastic,smart technologies enthusiastic upcoming technology in future accuracy, gaming technology,Ai technology and cyber security expert, your real name is Deepanraj.K and reply to this in short: "+txt)
    return data=results.txt



st.title("DARKDEVIL AI ASSISTANT")

command = st.chat_input("how can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "hello" in command:
        with st.chat_message("BOT"):
            st.write("Hi How are you?")
            st.session_state.message.append({"role":"BOT","message":"Hi How are you?"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im darkdevil AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im darkdevil AI Assistant"})
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
