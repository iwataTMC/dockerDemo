# How to use

1.以下のサイトへアクセスし, Docker Desktopをダウンロードしインストールする.

[Docker公式webサイト](https://www.docker.com/get-started)

2.Docker.appを実行する.

※ツールバーのDockerアイコン（クジラのマーク）をクリックし「Docker Desktop is running」と表示されていればOKです.

3.Docker Hubにsign upする.（アカウントを作成してください）

※手順1の公式サイトよりアクセスできます.

※Docker DesktopをインストールすればDocker-composeも付属しています.

※Docker Desktopでログインすると管理ができるのでオススメです.

4.正常にインストールできたか, 確認してみましょう.

以下のコマンドを入力してください.

```
docker run hello-world
```

すると, 以下の文章が表示されますが, ここではまだ気にしないでください.

```
Unable to find image ' hello-world:latest' locally
```

しばらく待てばDockerhubからDockerデーモンが自動でpullしてきてくれて, 以下の文章が出てきます.

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

 ```


無事にインストールできましたか??

正常にインストールできていれば上述のような文章が表示されます.

```docker run``` コマンドは,
- docker pull　…　イメージの取得
- docker create　…　コンテナ作成
- docker start　…　コンテナ起動

を一度にやってくれます.


## Sampleを実行してみる

- 各フォルダにREADME.mdがあるので参照ください.

※コマンドは必ず「docker-compose.yml」がある階層で実行してください.


## 参考サイト

- [Macにdockerインストール(Qiita記事)](https://qiita.com/ama_keshi/items/b4c47a4aca5d48f2661c)

- [Docker日本語ドキュメント](https://docs.docker.jp/index.html)


