import multiprocessing

# バインドするアドレスとポート
bind = '0.0.0.0:9000'

# ワーカーの数
workers = multiprocessing.cpu_count() * 2 + 1

# スレッドの数
threads = 2

# ワーカータイムアウト（秒）
timeout = 30

# デーモンモードで実行するかどうか
daemon = True

# ログファイルのパス
accesslog = '/usr/src/log/access.log'
errorlog = '/usr/src/log/error.log'

# ログレベル
loglevel = 'info'

# プロセス名
proc_name = 'prino'

# リクエストの最大サイズ（バイト）
limit_request_line = 4094

# アイドルワーカーのタイムアウト（秒）
worker_connections = 1000

# スタートアップ時のプロセス数
preload_app = True
