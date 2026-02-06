# coding: utf-8
"""
Chatアプリケーション
"""
import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st

class StreamHandler(BaseCallbackHandler):
    """
    LLMの返答をStreamingで取得するクラス
    """
    def __init__(self, container):
        """
        __init__
        
        :param self: self
        :param container: streamlitの書き込みコンテナ
        """
        self.container = container
        self.text = ""

    def on_llm_new_token(self, token:str, **kwargs):
        self.text += token
        self.container.markdown(self.text)

# Ollama接続のための環境設定読込
load_dotenv()
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "gemma3")
OLLAMA_SERVER_NAME = os.getenv("OLLAMA_SERVER_NAME", "localhost")
OLLAMA_SERVER_PORT = os.getenv("OLLAMA_SERVER_PORT", "11434")

SYSTEM_CONTENT = """
あなたは最新情報を正しく把握していません。最新情報について聞かれたらわからないことを伝えるか、最新情報ではないことを伝えてください。
"""


# Streamlit設定
st.set_page_config(page_title="LangChain Streaming Chat")
st.title("    LangChain × Streamlit Streaming Chat")

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
        handler = StreamHandler(placeholder)

        llm = ChatOllama(
            model=OLLAMA_MODEL_NAME,
            base_url=f"http://{OLLAMA_SERVER_NAME}:{OLLAMA_SERVER_PORT}",
            temperature=0.7,
            streaming=True,
            callbacks=[handler],
        )

        # LLMに渡すメッセージログを生成
        messages = []
        # システムメッセージを最初に追加
        messages.append(SystemMessage(content=SYSTEM_CONTENT))
        for role, content in st.session_state.messages:
            if role == "user":
                messages.append(HumanMessage(content=content))
            else:
                messages.append(AIMessage(content=content))
        # LLM実行
        llm.invoke(messages)

        # 返答後、履歴に追加
        st.session_state.messages.append(("assistant", handler.text))
