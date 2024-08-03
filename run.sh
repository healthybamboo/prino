#!/bin/bash
# === ORMのマーグレーション処理 ===
echo マイグレーションを実行中...
python manage.py migrate --settings=config.settings.production
echo マイグレーションを完了

# === 以下、Djangoの起動処理 ===
echo Djangoアプリケーションを起動中...
gunicorn config.wsgi:applicatio -c config/gunicorn.py
echo Djangoアプリケーションの起動を完了
