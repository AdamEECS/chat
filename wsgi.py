#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))


import redischat as main
application = main.configured_app()


# gunicorn -b '0.0.0.0:8002' wsgi --worker-class eventlet -w 1
# nohup gunicorn -b '0.0.0.0:3000' wsgi:app &
'''
注意：

1，使用gunicorn启动带stream的项目时，
worker_class应改为asyn（默认为sync）
建议改为eventlet或gevent
若从py文件读配置，参照本项目的格式

2，使用nginx做stream项目的服务器时，
proxy_buffering需要设置为off

'''
