import os
from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LangChainのセットアップ
def get_response(role, user_input):
    system_msg = SystemMessage(content=f"あなたは優秀な{role}の専門家です。ユーザーにわかりやすく説明してください。")
    user_msg = HumanMessage(content=user_input)

    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, api_key=api_key)
    return chat([system_msg, user_msg]).content

# Streamlit アプリUI
st.title("LLM専門家シミュレーター")
st.write("専門家を選び、質問してください。")

# 専門家の選択
role = st.radio("専門家の種類を選んでください：", ("医師", "エンジニア", "弁護士"))

# ユーザー入力
user_input = st.text_input("質問を入力してください：")

# 回答表示
if st.button("送信") and user_input:
    response = get_response(role, user_input)
    st.write("### 回答：")
    st.success(response)
