#!/bin/bash
# === ORMのマーグレーション処理 ===
echo マイグレーションを実行...
python manage.py migrate --settings=config.settings.production
# ステータスコードが0以外の場合はエラー終了
if [ $? -ne 0 ]; then
  exit 1
fi
echo マイグレーションを完了


# === 以下、Djangoの起動処理 ===
echo Djangoアプリケーションを起動中...
gunicorn config.wsgi:application \
  --bind 0.0.0.0:9000 \
  --timeout 30 \
  --log-level info \
  --limit-request-line 4094 \
  --worker-connections 1000 \
  --preload