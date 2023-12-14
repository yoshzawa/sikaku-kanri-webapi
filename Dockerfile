# ベースイメージを指定
FROM python:3.9

# 必要なパッケージをインストール
RUN pip install fastapi uvicorn mysql-connector-python

# Gitが必要ならインストールする
RUN apt-get update && apt-get install -y git

# 作業ディレクトリを設定
WORKDIR /app

# GitHubからソースコードをクローン
RUN git clone https://github.com/yoshzawa/sikaku-kanri-webapi.git .

# 設定ファイルからMySQL接続情報をコピー
COPY config.json /app/config.json

# 作業ディレクトリを設定
WORKDIR /app/app

# FastAPIアプリケーションを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
