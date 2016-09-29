from . import ModelMixin
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    deleted = db.Column(db.Boolean, default=False)

    chats = db.relationship('Chat', backref="user")

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    # 验证注册用户的合法性的
    def valid(self):
        valid_username = User.query.filter_by(username=self.username).first() == None
        valid_username_len = 6 <= len(self.username) <= 20
        valid_password_len = 6 <= len(self.password) <= 20
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 6, 小于等于 20'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 6, 小于等于 20'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs
