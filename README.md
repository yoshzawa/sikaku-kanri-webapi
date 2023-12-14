# 資格試験管理システム WebAPI部分
システム開発の授業で作成する課題のサンプルです

## 利用方法

* Ubuntu Serverにdocker、gitをインストール
* 「git clone https://github.com/yoshzawa/sikaku-kanri-webapi.git 」などして、ソースをcloneする
* 「cd sikaku-kanri-webapi/」などして、ソースのフォルダに移動する
* 「sudo docker build -t my_webapi .」のような感じで、docker buildする
* 「sudo docker run -it -p 8888:8000 --name mycontainer my_webapi0」のような感じで、Containerを起動する
* ブラウザーで、「http://docker-server:8888/ 」にアクセスする。containerの中ではポート8000だが、containerの外では8888で接続する。
* 「{"detail":"Not Found"}」と表示されればOK
* ブラウザーで、「http://docker-server:8888/sikaku/list 」にアクセスする。
* ブラウザーで、「http://docker-server:8888/voucher/list 」にアクセスする。
* ブラウザーで、「http://docker-server:8888/sikaku/docs 」にアクセスする。
* ブラウザーで、「http://docker-server:8888/voucher/docs 」にアクセスする。

## ヒント
* docker buildで「--progress=plain」オプションを付ける
* docker runで[--rm」オプションを付ける
