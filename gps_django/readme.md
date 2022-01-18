## 前提
以下のコマンドがインストール済みである。

* docker
* docker-compose

## 使い方
1. 以下のコマンドでビルドを行う。

    ```bash
    docker-compose build
    ```
1. プロジェクトが未作成であれば、以下のコマンドでプロジェクトを作成する。ここでは、sample_gpsとする。

    ```bash
    # 一度だけ実行（末尾のピリオドを忘れないこと）
    docker run --rm --name once_django -v ${PWD}/src:/code -it custom_django django-admin startproject sample_gps .
    # root権限で作成されるので、所有者を変更
    sudo chown -R ${USER}:${USER} src/*
    ```

1. 下記を実施する。
    * 下記のファイルをエディタで開く。

        ```bash
        src/sample_gps/settings.py
        ```

    * 以下の部分を修正する。

        ```python
        # ======
        # 変更前
        # ======
        ALLOWED_HOSTS = []

        # ======
        # 変更後
        # ======
        ALLOWED_HOSTS = ['*']
        ```
1. ブラウザで以下のサイトを開き、「The install worked successfully! Congratulations!」が表示されれば成功。

    ```bash
    http://<マシンのIPアドレス>:8780
    ```


1. アプリが未作成であれば、以下のコマンドでアプリを作成する。ここでは、gpsとする。

    ```bash
    # 各自、必要なアプリを作ること
    docker run --rm --name once_django -v ${PWD}/src:/code -it custom_django python manage.py startapp gps
    # root権限で作成されるので、所有者を変更
    sudo chown -R ${USER}:${USER} src/gps
    ```
