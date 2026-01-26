# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend
# Ia que vamos usar: OpenAI
# pip install openai streamlit
# Hugging Face (pra construção de IA personalizada -> aprender)

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

modelo_ia = OpenAI()

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

try:
    if texto_usuario:
        st.chat_message("user").write(texto_usuario)
        mensagem_usuario = {"role": "user", "content": texto_usuario}
        st.session_state["lista_mensagens"].append(mensagem_usuario)


        resposta_ia = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"], model="gpt-4o"
        )
        texto_resposta_ia = resposta_ia.choices[0].message.content
        
        st.chat_message("assistant").write(texto_resposta_ia)
        mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)

except Exception as e:
    st.error("⚠️ Erro ao chamar a API da OpenAI")
    st.exception(e)