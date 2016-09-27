# chat

# 安装需求

apt-get install redis-server
pip3 install python-redis gunicorn

# 如果执行上述安装报错，尝试下面两项
apt-get install build-essential
apt-get install python3-dev

# 开启redis
redis-server&
# 使用 gunicorn 启动
gunicorn --worker-class=gevent -t 9999 redischat:app -b 0.0.0.0:3000
# 开启 debug 输出
gunicorn --log-level debug --worker-class=gevent -t 999 redis_chat81:app
# 把 gunicorn 输出写入到 gunicorn.log 文件中
gunicorn --log-level debug --access-logfile gunicorn.log --worker-class=gevent -t 999 redis_chat81:app
