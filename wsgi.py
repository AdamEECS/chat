#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

sys.path.insert(0, abspath(dirname(__file__)))


import redischat as main
application = main.configured_app()


# gunicorn -b '0.0.0.0:3000' wsgi:app
# nohup gunicorn -b '0.0.0.0:3000' wsgi:app &
