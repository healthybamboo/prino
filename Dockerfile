# Django環境用のDockerfile
FROM python:3.11 as base
USER root

# タイムゾーン設定
ENV TZ Asia/Tokyo

# ベースイメージに対してコマンドを実行
RUN apt-get update && \
    apt-get install -y \
    vim \
    less \
    git \
    && rm -rf /var/lib/apt/lists/* 

#  日本語とタイムゾーンの設定
ENV LANGUAGE ja_JP:ja
ENV TZ JST-9

# 設定情報(UID,GIDについてはidコマンドでdockerの実行ユーザーと合わせた方がよい)
ARG USERNAME=prino
ARG GROUPNAME=prino
ARG UID=1000
ARG GID=1000
ARG STATIC_DIR=/usr/src/static
ARG WORKDIR=/usr/src/app

ENV PYTHONPATH $WORKDIR

# 作業ディレクトリ設定
WORKDIR $WORKDIR


# ユーザー関連の設定
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME && \
    mkdir -p $WORKDIR && \
    mkdir -p $STATIC_DIR && \
    chown -R $UID:$GID $WORKDIR && \
    chown -R $UID:$GID $STATIC_DIR

# ユーザーのbinaryディレクトリをパスに追加
ENV PATH /home/$USERNAME/.local/bin:$PATH
# ユーザー切り替え
USER $USERNAME

# パッケージインストール
COPY requirements.txt $WORKDIR
RUN  pip install --upgrade pip && \
    pip install -r requirements.txt


# 開発ビルド用の設定
FROM base as dev


# 本番ビルド用の設定
FROM base as prod

# プロジェクトのコードをコピー
COPY . $WORKDIR

# 静的ファイルのコピー
RUN python manage.py collectstatic --noinput

# サーバーを起動
CMD ["sh","run.sh"]