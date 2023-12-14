# Python用のDockerfile
FROM python:3.9
USER root

# タイムゾーン設定
ENV TZ Asia/Tokyo

# ベースイメージに対してコマンドを実行
RUN apt-get update 
RUN apt-get install -y \
    vim \
    less \
    git \
    && rm -rf /var/lib/apt/lists/* 

#  日本語とタイムゾーンの設定
ENV LANGUAGE ja_JP:ja
ENV TZ JST-9

# 設定情報(UID,GIDについてはidコマンドでdockerの実行ユーザーと合わせた方がよい)
ARG USERNAME=vscode
ARG GROUPNAME=vscode
ARG UID=1000
ARG GID=1000
ARG WORKDIR=/usr/src/app

ENV PYTHONPATH $WORKDIR

# 作業ディレクトリ設定
WORKDIR $WORKDIR

# --- ユーザー関連の設定 ---
# ユーザー追加
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
# フォルダ作成＆管理者設定
RUN mkdir -p $WORKDIR
RUN chown -R $UID:$GID $WORKDIR
# ユーザーのbinaryディレクトリをパスに追加
ENV PATH /home/$USERNAME/.local/bin:$PATH
# ユーザー切り替え
USER $USERNAME
# -----------------------


## --- アプリケーション用の環境設定 ---
# 初期化用のスクリプトをコピー
COPY init.sh /script/
COPY wait-for-it.sh /script/

# パッケージインストール
COPY requirements.txt $WORKDIR
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN python -m pip install --user -r requirements.txt
 # -----------------------