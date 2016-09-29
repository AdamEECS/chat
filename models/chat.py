from . import ModelMixin
from . import db
from . import timestamp


class Chat(db.Model, ModelMixin):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    created_time = db.Column(db.Integer)
    channel = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, form):
        print('chat init', form)
        self.content = form.get('content', '')
        self.channel = form.get('channel', '')
        self.created_time = timestamp()
