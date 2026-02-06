# coding: utf-8
"""
Chatアプリケーション
"""
import streamlit as st

from dotenv import load_dotenv

# Ollama接続のための環境設定読込
load_dotenv()

# Streamlit設定
st.set_page_config(page_title="Chat")
st.title("Chat")
