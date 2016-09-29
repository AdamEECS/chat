from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort
from flask import Response
from functools import wraps
from models.user import User
import time
import json


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        u = current_user()
        print('login required', u)
        if u is None:
            print('not login')
            return redirect(url_for('.login_index'))
        return f(*args, **kwargs)
    return function
