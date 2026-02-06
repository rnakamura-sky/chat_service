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

## 備考
- 外部の`Ollama`を使用するときに、プロキシが問題となることがあります。
  streamlitを起動する前に、プロキシの環境変数を設定しなおして起動してください。
- .envファイルを作成して下記の設定を変更して実行することができます。（記載している値は、デフォルト値）
  ```
  OLLAMA_MODEL_NAME=gemma3      # 使用するモデル名
  OLLAMA_SERVER_NAME=localhost  # Ollamaのサーバー名
  OLLAMA_SERVER_PORT=11434      # Ollamaのポート
  ```

