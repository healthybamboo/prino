#!/bin/bash
# === ORMのマーグレーション処理 ===
echo マイグレーションを実行
python manage.py migrate --settings=config.settings.production
echo マイグレーションを完了

echo 親カテゴリーの追加を実行
python manage.py loaddata ./threads/fixtures/parent_category.json --settings=config.settings.production
echo 親カテゴリーの追加を完了

echo 子カテゴリーを追加を実行
python manage.py loaddata ./threads/fixtures/category.json --settings=config.settings.production
echo 子カテゴリーを追加を完了

# === 以下、Djangoの起動処理 ===
echo Djangoアプリケーションを起動...
gunicorn config.wsgi:applicatio -c config/gunicorn.py
echo Djangoアプリケーションを起動しました
