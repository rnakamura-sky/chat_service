チャットサービスです

全てをローカルで完結できるよう、Ollamaを使用する想定です。

UIは簡単に実装できるようStreamlitを使用します。


## 使用機能（パッケージ）
- LangChain
- Streamlit

## 前提
- 利用可能なOllamaサービスが立ち上がっている（ローカルでも外部でもOK）

## 実行方法
```bash
# プロジェクトフォルダで実行
# ローカルのみ動作させる場合
streamlit run src/app.py

# 社内展開する場合
# ※合わせて端末のファイアウォール設定を行う必要があります。
#   ポートはstreamlitのデフォルトポート想定
streamlit run src/app.py --server.adress 0.0.0.0 --server.port 8501
```
