import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .env から環境変数を読み込む
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit アプリの UI
st.title("専門家 LLM アプリ")
st.write("このアプリでは、選んだ専門家の視点で質問に回答します。")

# ラジオボタンで専門家の種類を選択
role = st.radio("専門家の種類を選んでください：", ("医者", "弁護士", "歴史学者"))

# ユーザーの質問を受け取る
user_input = st.text_input("質問を入力してください:")

# LLM に問い合わせる関数
def ask_expert(user_input, role):
    os.environ["OPENAI_API_KEY"] = openai_api_key  # ← ここで環境変数に明示的にセット

    system_msg = {
        "医者": "あなたは経験豊富な医者です。医学的な見地から専門的に答えてください。",
        "弁護士": "あなたは熟練の弁護士です。法律に基づいて簡潔に説明してください。",
        "歴史学者": "あなたは歴史に精通した学者です。史実と文献に基づいて丁寧に解説してください。"
    }[role]

    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5
    )

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_input)
    ]

    response = chat(messages)
    return response.content

# 実行処理と画面表示
if user_input:
    with st.spinner("専門家が回答中..."):
        answer = ask_expert(user_input, role)
        st.markdown("### 回答：")
        st.write(answer)
