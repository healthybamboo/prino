# Primo
PrimeVideoの動画更新を通知するDiscordBot

## 使い方

### WEBHOOK_URLの設定
```production.py
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/xxxxxxxxxxx'
```

### サーバーの起動
```
 python manage.py runserver 0.0.0.0:9000 --settings=config.settings.production --noreload
```


### build
```
docker build -t prino:latest --target prod .  
```
