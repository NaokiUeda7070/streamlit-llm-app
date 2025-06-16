<<<<<<< HEAD
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
=======
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数（.env）を読み込む
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit アプリのUI
st.title("専門家 LLM アプリ")
st.write("このアプリでは、選んだ専門家の視点で質問に回答します。")

# ラジオボタンで専門家の種類を選択
role = st.radio("専門家の種類を選んでください：", ("医者", "弁護士", "歴史学者"))

# ユーザーの質問を受け取る
user_input = st.text_input("質問を入力してください:")

# LLMに問い合わせる関数
def ask_expert(user_input, role):
    system_msg = {
        "医者": "あなたは経験豊富な医者です。医学的な見地から専門的に答えてください。",
        "弁護士": "あなたは熟練の弁護士です。法律に基づいて簡潔に説明してください。",
        "歴史学者": "あなたは歴史に精通した学者です。史実と文献に基づいて丁寧に解説してください。"
    }[role]

    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5,
        openai_api_key=openai_api_key
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
>>>>>>> 17ea4910785410fccbf9f48bbf9898d0e6e6768a
