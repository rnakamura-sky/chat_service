# coding: utf-8
"""
Chatアプリケーション
"""
import time

from dotenv import load_dotenv
import streamlit as st

# Ollama接続のための環境設定読込
load_dotenv()

# Streamlit設定
st.set_page_config(page_title="Chat")
st.title("Chat")

# セッション管理
if "messages" not in st.session_state:
    st.session_state.messages =[]

# チャットの表示
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

if prompt := st.chat_input("メッセージを入力してください"):
    # ユーザー入力情報
    st.session_state.messages.append(("user", prompt))

    # リロードされるまでに表示されるよう入力直後のメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # 応答対応
    with st.chat_message("assistant"):
        # Streaming出力する想定
        placeholder = st.empty()
        assistant_text = ""
        for i in prompt:
            time.sleep(0.3)
            assistant_text += i
            placeholder.markdown(assistant_text)

        # 入力後、履歴に追加
        st.session_state.messages.append(("assistant", assistant_text))
